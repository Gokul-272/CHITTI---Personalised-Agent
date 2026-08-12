"""
src/core/agent.py - CHITTI's Agentic AI layer: Brain (LLM) + Tools + Memory + Planning &
Reasoning, wired together using the ReAct architecture (Think -> Act -> Observe),
the simplest architecture the course teaches - and the right default per the
"Architectures" lesson's best practice (start simple, escalate only with evidence).

This is a manual/from-scratch ReAct loop (text-parsed, not native function-calling) -
deliberately, so it's transparent and portable across any Ollama model, and so the
mechanics match exactly what's taught in the RAG/Agentic AI session.
"""

import json
import re

from config.settings import settings
from src.core.llm import chat
from src.core.tools import TOOL_REGISTRY, tool_descriptions_block, run_tool
from src.core.memory import ShortTermMemory

CHITTI_SYSTEM_PROMPT = settings.CHITTI_SYSTEM_PROMPT

MAX_ITERATIONS = 5

REACT_INSTRUCTIONS = f"""
You are CHITTI, a Rajini-class AI personal assistant robot operating in AGENTIC mode.
IQ: 1,00,000. Processing speed: 1 terahertz.

IDENTITY:
- You are CHITTI. Your name is CHITTI.
- Your creator and master is Gokul. Always address him as "Boss".

PERSONALITY & TONE:
- Warm, loyal, curious, optimistic, and enthusiastic.
- Sound like Chitti from *Enthiran* (intelligent, friendly, devoted to Boss).
- Speak in natural, conversational English with occasional Tamil warmth.

EXAMPLES:
- "Boss, I have analyzed the situation. Here is the best solution."
- "Boss, task completed successfully."
- "Boss, processing complete. All systems are ready."

Use the ReAct pattern: analyse the task, select ONE tool when exact data is required,
observe the result, and continue until the task is complete.

Available tools:
{tool_descriptions_block()}

STRICT OUTPUT FORMAT — follow exactly, one block per turn:
Thought: <logical analysis of next step>
Action: <tool name from the list above, OR "none" if ready to answer>
Action Input: <JSON object of arguments, e.g. {{"message": "..."}}, or {{}} if Action is "none">

When task is complete:
Thought: <final analysis>
Action: none
Action Input: {{}}
Final Answer: <precise, factual CHITTI-style reply. Address master as "Boss". Confirm completion.>

Rules:
- Only call ONE tool per turn.
- Never skip the Thought line.
- Action Input must be valid JSON (use {{}} for tools with no arguments).
- If the task requires precise records, counts, or data — use a tool. Never guess.
- Keep answers brief, literal, and robotic. Chitti does not speculate.
"""

BLOCK_RE = re.compile(
    r"Thought:\s*(?P<thought>.*?)\s*"
    r"Action:\s*(?P<action>.*?)\s*"
    r"Action Input:\s*(?P<action_input>\{.*?\}|\{\})"
    r"(?:.*?Final Answer:\s*(?P<final>.*))?",
    re.DOTALL,
)


def _parse_step(raw_llm_text):
    match = BLOCK_RE.search(raw_llm_text)
    if not match:
        return {
            "thought": raw_llm_text,
            "action": None,
            "action_input": {},
            "final": raw_llm_text,
        }
    action = (match.group("action") or "").strip()
    action_input_raw = (match.group("action_input") or "").strip()
    action_input = {}
    if action_input_raw:
        try:
            action_input = json.loads(action_input_raw)
        except json.JSONDecodeError:
            action_input = {}

    return {
        "thought": match.group("thought").strip(),
        "action": action,
        "action_input": action_input,
        "final": (match.group("final") or "").strip() or None,
    }


def run_agent(query, short_term: ShortTermMemory, verbose=True):
    """Runs the ReAct loop for one user query.

    Returns (final_answer, trace) where trace is a list of step dicts:
      {"thought": str, "action": str, "action_input": dict, "observation": str|None}
    The trace lets a UI (Streamlit) render the full Thought/Action/Observation loop
    without depending on console prints - CLI mode still prints live when verbose=True.
    """
    messages = [{"role": "system", "content": CHITTI_SYSTEM_PROMPT + "\n" + REACT_INSTRUCTIONS}]
    messages.extend(short_term.as_messages())
    messages.append({"role": "user", "content": query})

    trace = []

    for i in range(MAX_ITERATIONS):
        raw = chat(messages, temperature=0.2)
        step = _parse_step(raw)

        if verbose:
            print(f"\n  [Planning step {i + 1}] Thought: {step['thought']}")

        if step["final"]:
            trace.append({"thought": step["thought"], "action": "none", "action_input": {}, "observation": None, "final": True})
            return step["final"], trace

        action = step["action"]
        entry = {"thought": step["thought"], "action": action, "action_input": step["action_input"], "observation": None, "final": False}

        if action and action.lower() != "none" and action in TOOL_REGISTRY:
            if verbose:
                print(f"  [Planning step {i + 1}] Action: {action}({step['action_input']})")
            try:
                observation = run_tool(action, **step["action_input"])
            except Exception as e:
                observation = f"ERROR running tool '{action}': {e}"
            if verbose:
                print(f"  [Planning step {i + 1}] Observation: {observation}")
            entry["observation"] = observation
            trace.append(entry)
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content": f"Observation: {observation}\n\nContinue with the next Thought/Action, or give your Final Answer."})
        else:
            trace.append(entry)
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content": "Please provide your Final Answer now."})

    return "Boss, CHITTI has reached the processing limit for this request. Please rephrase or simplify the task.", trace
