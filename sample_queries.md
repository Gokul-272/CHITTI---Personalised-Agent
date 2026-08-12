# Sample Queries - CHITTI Assistant

Run `python -m scripts.ingest` once, then launch `streamlit run src/ui/streamlit_app.py`
(or use `python -m src.ui.cli --mode rag` / `--mode agent` for the terminal version). Each
query below is picked to showcase a specific concept from the course.

## RAG Mode

RAG should only ever **reply** - watch for that. It never takes an action.

| Query | What it showcases |
|---|---|
| `Say something witty about Boss's coffee habit.` | Retrieval from personality docs - sentence-level chunking. |
| `What happened during the Extremis Threat Containment mission?` | Retrieval from `mission_briefings.md` - Markdown header-aware chunking, outcome and lessons learned stay together. |
| `What is Pepper Potts' role and dossier summary?` | Retrieval from `personnel_dossiers.json` - proves JSON was parsed with `json.load` into clean per-record chunks. |
| `What was the resolution for the Mark 42's flight thruster fault on 2024-03-15?` | Retrieval from `operation_logs.csv` - proves CSV rows were parsed with column headers via `csv.DictReader`. |
| `Walk me through the House Party protocol.` | Retrieval from `command_protocols.html` - proves HTML tags were stripped during chunking. |
| `What is Boss's favorite color?` | **Should say it doesn't know** - this isn't in the knowledge base. Confirms CHITTI isn't hallucinating past retrieved context. |

## Agentic Mode

In the Streamlit UI, open the "See CHITTI's reasoning" expander under each reply to
watch the ReAct loop (Thought / Action / Observation) - that's the same trace shown in CLI mode.

| Query | What it showcases |
|---|---|
| `Check the Mark 42's status and alert me if anything needs attention.` | Tool call chaining: `check_suit_status` -> reasons about the result -> `send_alert`. This is "Agentic RAG" - retrieval used as a tool call mid-plan. |
| `Remind me to recalibrate the repulsors tomorrow at 9am.` | A single clean tool call: `schedule_reminder`. |
| `Look up how the Mark 42 handled the drone swarm, then let the team know if we should use the same tactic today.` | Multi-step planning: `lookup_knowledge_base` (combat strategy) -> reasoning -> `send_alert` with a summary. Shows Planning & Reasoning composing two tools toward one goal. |
| `Remember that I'm allergic to shellfish.` | `remember_fact` - writes to long-term memory (`long_term_memory.json`). |
| `What do you remember about my allergies?` | `recall_fact` - reads back what was persisted in the query above. Restart the app (or clear the conversation and reopen it in a new session) to prove it's genuinely persistent, not just short-term context. |
| `What have you done for me so far?` | `view_action_log` - episodic memory: a structured log of every action taken this session. |
| `What's 947 times 812?` | Should give a **Final Answer directly with no tool call** - there's no tool for arbitrary math in this demo, so it should reason it out or say so, not hallucinate a tool. Good for showing the model correctly deciding "Action: none." |

## What to Point Out Live

- In **RAG mode**, the caption under each answer ("Retrieved from: ...") is proof the
  answer is grounded, not memorized.
- In **Agentic mode**, open the reasoning expander before reading the final answer aloud
  - that's the whole ReAct architecture, visible in real time, in the same UI the
  interns will use for their own assignment.
- Try the shellfish `remember_fact` / `recall_fact` pair, then use the sidebar's
  "Clear conversation" button (which resets short-term memory) and ask about allergies
  again - it should still know, proving long-term memory survives independently of the
  visible chat history.
