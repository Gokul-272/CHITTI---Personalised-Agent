"""
src/core/tools.py - CHITTI's agentic Tools layer.

Each tool is a plain Python function with a clear, narrow scope (per the course's
"one tool = one clearly-scoped capability" best practice), plus a risk_level used to
decide whether an action needs confirmation before running (human-in-the-loop).

Actions here are SIMULATED - per the course spec, an "action" just prints/returns an
alert message showing the action was taken. No real hardware, no real notifications.
"""

from datetime import datetime

from src.core.vector_store import retrieve
from src.core.rag import format_context
from src.nl2sql.pipeline import answer as nl2sql_answer
import src.core.memory as memory_module


def tool_query_operations_db(question: str) -> str:
    """Mission-oriented read-only operational lookup using the structured operations database."""
    return tool_query_fleet_database(question)


def tool_check_equipment_status(equipment: str = "all") -> str:
    """Read-only equipment check using operation logs and related command protocols."""
    query = f"status of equipment {equipment}"
    chunks = retrieve(query, top_k=5)
    if not chunks:
        return f"Boss, no status data found for {equipment} in CHITTI's database."
    lines = []
    for i, c in enumerate(chunks, 1):
        lines.append(f"[{i}] (source: {c['doc_type']}) {c['text']}")
    return "\n".join(lines)


def tool_schedule_operation(operation: str, when: str = "as ordered") -> str:
    """Schedule an operation or mission with a concise operational note."""
    ts = datetime.now().strftime("%H:%M:%S")
    entry = f"[{ts}] OPERATION SCHEDULED for {when}: {operation}"
    ACTION_LOG.append(entry)
    print(f"\n  >> {entry}\n")
    return f"Boss, operation '{operation}' has been logged and scheduled for {when}. Task confirmed."


def tool_remember_preference(key: str, value: str) -> str:
    """Persist a mission preference or trusted team configuration for future operations."""
    return memory_module.remember(key, value)


# In-memory "episodic" log of actions taken this session - a crude but real example of
# the Memory component (episodic memory) feeding back into what the agent can report.
ACTION_LOG = []


def tool_check_suit_status(suit: str = "all") -> str:
    """Read-only tool. Risk: none. Looks up suit diagnostics from the knowledge base."""
    return tool_check_equipment_status(suit)


def tool_send_alert(message: str) -> str:
    """Reversible, low-stakes action. Simulated - just logs and returns a confirmation
    string. In a real system this might page a team or push a notification."""
    ts = datetime.now().strftime("%H:%M:%S")
    entry = f"[{ts}] ALERT SENT: {message}"
    ACTION_LOG.append(entry)
    print(f"\n  >> {entry}\n")
    return f"Boss, alert dispatched: '{message}'. Transmission confirmed."



def tool_schedule_reminder(text: str, when: str = "unspecified time") -> str:
    """Reversible, low-stakes action. Simulated - logs and confirms."""
    return tool_schedule_operation(text, when)



def tool_lookup_knowledge_base(query: str) -> str:
    """Read-only tool. Risk: none. This is the RAG retriever exposed AS a tool, so the
    agent can look things up mid-plan (e.g. 'check how the Mark 42 handled X, then act')."""
    chunks = retrieve(query, top_k=4)
    return format_context(chunks)


def tool_query_fleet_database(question: str) -> str:
    """Read-only tool. Risk: none. Answers precise/aggregate questions (counts, sums,
    averages, joins across suits/technicians/maintenance/missions) from the structured
    PostgreSQL fleet-ops database via the NL2SQL pipeline (src/nl2sql) - the counterpart
    to lookup_knowledge_base for anything the narrative vector KB can't reliably count."""
    result = nl2sql_answer(question)
    if result.get("error"):
        return f"Could not safely answer from structured records: {result['error']}"
    return f"SQL used: {result['sql']}\n\nAnswer: {result['answer']}"


def tool_view_action_log() -> str:
    """Read-only tool. Shows everything the agent has done this session (episodic memory)."""
    if not ACTION_LOG:
        return "No actions taken yet this session."
    return "\n".join(ACTION_LOG)


# Tool registry: name -> (function, description, risk_level, requires_confirmation)
# Descriptions are written precisely on purpose - the course's "Tools" lesson mistake
# story is exactly a vaguely-described tool getting called for the wrong job.
TOOL_REGISTRY = {
    "query_operations_db": {
        "fn": tool_query_operations_db,
        "description": "Query the structured operations database for exact mission counts, totals, averages, and mission-history facts. Use this whenever the answer requires precise operational records rather than a narrative summary. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "check_equipment_status": {
        "fn": tool_check_equipment_status,
        "description": "Check equipment, suit, or system readiness using diagnostic and operational records. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "schedule_operation": {
        "fn": tool_schedule_operation,
        "description": "Schedule an operation or mission with a concise operational note. Simulated and reversible, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "remember_preference": {
        "fn": tool_remember_preference,
        "description": "Persist a mission preference, trusted team member, or operating style for follow-up tasks. Low-stakes and reversible.",
        "risk": "low",
        "confirm": False,
    },
    "check_suit_status": {
        "fn": tool_check_suit_status,
        "description": "Look up diagnostic/telemetry data for a suit (e.g. 'Mark 42', 'Mark 45', or 'all'). Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "send_alert": {
        "fn": tool_send_alert,
        "description": "Send an alert/notification message. Simulated - prints and logs the alert, no real paging. Reversible, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "schedule_reminder": {
        "fn": tool_schedule_reminder,
        "description": "Schedule a reminder with text and an optional time. Simulated - prints and logs it. Reversible, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "lookup_knowledge_base": {
        "fn": tool_lookup_knowledge_base,
        "description": "Search CHITTI's full knowledge base (project briefings, Gokul's memory profile, operation logs, system protocols) for technical or personal information. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "query_fleet_database": {
        "fn": tool_query_fleet_database,
        "description": "Query the structured fleet-operations database (suits, technicians, maintenance history, missions) for precise counts, sums, averages, or joins - e.g. 'how many times has the Mark 42 needed thruster repairs' or 'average mission duration at threat level 5'. Use this instead of lookup_knowledge_base whenever the question needs an exact number or an aggregate across many records. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "view_action_log": {
        "fn": tool_view_action_log,
        "description": "View a log of every action taken so far this session. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "remember_fact": {
        "fn": lambda key, value: memory_module.remember(key, value),
        "description": "Persist a durable fact to long-term memory, e.g. key='allergy', value='shellfish'. Reversible, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "recall_fact": {
        "fn": lambda key: memory_module.recall(key),
        "description": "Recall a previously remembered fact by key from long-term memory. Read-only.",
        "risk": "none",
        "confirm": False,
    },
}


def tool_descriptions_block():
    """A formatted block of tool names + descriptions, for the ReAct system prompt."""
    lines = []
    for name, spec in TOOL_REGISTRY.items():
        lines.append(f"- {name}({_signature_hint(name)}): {spec['description']}")
    return "\n".join(lines)


def _signature_hint(name):
    hints = {
        "query_operations_db": "question",
        "check_equipment_status": "equipment='all'",
        "schedule_operation": "operation, when='as ordered'",
        "remember_preference": "key, value",
        "check_suit_status": "suit='all'",
        "send_alert": "message",
        "schedule_reminder": "text, when='unspecified time'",
        "lookup_knowledge_base": "query",
        "query_fleet_database": "question",
        "view_action_log": "",
        "remember_fact": "key, value",
        "recall_fact": "key",
    }
    return hints.get(name, "")


def run_tool(name, **kwargs):
    if name not in TOOL_REGISTRY:
        return f"ERROR: no such tool '{name}'. Available tools: {', '.join(TOOL_REGISTRY.keys())}"
    return TOOL_REGISTRY[name]["fn"](**kwargs)
