"""
src/core/tools.py - CHITTI's agentic Tools layer for Personal Assistant workflow.

Each tool is a plain Python function with a clear, narrow scope, plus a risk_level used to
decide whether an action needs confirmation before running (human-in-the-loop).

Actions here are SIMULATED - an "action" logs and returns a confirmation message.
"""

from datetime import datetime

from src.core.vector_store import retrieve
from src.core.rag import format_context
from src.nl2sql.pipeline import answer as nl2sql_answer
import src.core.memory as memory_module


ACTION_LOG = []


def tool_query_personal_db(question: str) -> str:
    """Read-only tool. Answers precise questions (counts, totals, averages, filtering) from the
    structured Personal Assistant PostgreSQL database (tasks, schedule_events, contacts, expenses,
    personal_notes) via the NL2SQL pipeline."""
    result = nl2sql_answer(question)
    if result.get("error"):
        return f"Could not safely answer from structured personal records: {result['error']}"
    return f"SQL used: {result['sql']}\n\nAnswer: {result['answer']}"


def tool_query_operations_db(question: str) -> str:
    """Alias for tool_query_personal_db."""
    return tool_query_personal_db(question)


def tool_query_fleet_database(question: str) -> str:
    """Alias for tool_query_personal_db."""
    return tool_query_personal_db(question)


def tool_check_task_status(item: str = "all") -> str:
    """Read-only task/schedule status check using knowledge base and personal records."""
    query = f"status of {item}"
    chunks = retrieve(query, top_k=5)
    if not chunks:
        return f"Boss, no status records found for {item} in CHITTI's database."
    lines = []
    for i, c in enumerate(chunks, 1):
        lines.append(f"[{i}] (source: {c['doc_type']}) {c['text']}")
    return "\n".join(lines)


def tool_check_equipment_status(equipment: str = "all") -> str:
    """Alias for tool_check_task_status."""
    return tool_check_task_status(equipment)


def tool_check_suit_status(suit: str = "all") -> str:
    """Alias for tool_check_task_status."""
    return tool_check_task_status(suit)


def tool_schedule_personal_event(event: str, when: str = "unspecified time") -> str:
    """Schedule a personal event, reminder, or task note."""
    ts = datetime.now().strftime("%H:%M:%S")
    entry = f"[{ts}] EVENT SCHEDULED for {when}: {event}"
    ACTION_LOG.append(entry)
    print(f"\n  >> {entry}\n")
    return f"Boss, event '{event}' has been logged and scheduled for {when}. Task confirmed."


def tool_schedule_operation(operation: str, when: str = "as ordered") -> str:
    """Alias for tool_schedule_personal_event."""
    return tool_schedule_personal_event(operation, when)


def tool_schedule_reminder(text: str, when: str = "unspecified time") -> str:
    """Schedule a reminder with text and an optional time."""
    return tool_schedule_personal_event(text, when)


def tool_remember_preference(key: str, value: str) -> str:
    """Persist a personal preference or work-style setting for future interaction."""
    return memory_module.remember(key, value)


def tool_send_alert(message: str) -> str:
    """Send an alert/notification message. Simulated - logs and confirms."""
    ts = datetime.now().strftime("%H:%M:%S")
    entry = f"[{ts}] ALERT SENT: {message}"
    ACTION_LOG.append(entry)
    print(f"\n  >> {entry}\n")
    return f"Boss, alert dispatched: '{message}'. Transmission confirmed."


def tool_lookup_knowledge_base(query: str) -> str:
    """Search CHITTI's vector knowledge base (profile, coding style, preferences, goals, work-style) for contextual information."""
    chunks = retrieve(query, top_k=4)
    return format_context(chunks)


def tool_view_action_log() -> str:
    """Shows everything the agent has done this session (episodic memory)."""
    if not ACTION_LOG:
        return "No actions taken yet this session."
    return "\n".join(ACTION_LOG)


# Tool registry: name -> spec
TOOL_REGISTRY = {
    "query_personal_db": {
        "fn": tool_query_personal_db,
        "description": "Query the structured Personal Assistant database (tasks, schedule_events, contacts, expenses, personal_notes) for exact counts, sums, averages, or filtering. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "query_operations_db": {
        "fn": tool_query_operations_db,
        "description": "Query structured personal database for tasks, events, expenses, and contacts facts. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "query_fleet_database": {
        "fn": tool_query_fleet_database,
        "description": "Query structured personal database for exact counts, sums, or joins across tasks/expenses/events. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "check_task_status": {
        "fn": tool_check_task_status,
        "description": "Check task readiness, project status, or schedule progress. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "check_equipment_status": {
        "fn": tool_check_equipment_status,
        "description": "Check equipment/task status using diagnostic and operational records. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "check_suit_status": {
        "fn": tool_check_suit_status,
        "description": "Look up diagnostic or system readiness status. Read-only.",
        "risk": "none",
        "confirm": False,
    },
    "schedule_personal_event": {
        "fn": tool_schedule_personal_event,
        "description": "Schedule a personal event, meeting, or task with a concise note. Simulated, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "schedule_operation": {
        "fn": tool_schedule_operation,
        "description": "Schedule an operation or task note. Simulated and reversible, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "schedule_reminder": {
        "fn": tool_schedule_reminder,
        "description": "Schedule a reminder with text and an optional time. Simulated, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "remember_preference": {
        "fn": tool_remember_preference,
        "description": "Persist a personal preference, contact rule, or operating style for follow-up tasks. Reversible, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "send_alert": {
        "fn": tool_send_alert,
        "description": "Send an alert/notification message to Boss. Simulated, low-stakes.",
        "risk": "low",
        "confirm": False,
    },
    "lookup_knowledge_base": {
        "fn": tool_lookup_knowledge_base,
        "description": "Search CHITTI's vector knowledge base (Gokul's profile, preferences, coding style, goals, work-style) for personal or technical information. Read-only.",
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
        "query_personal_db": "question",
        "query_operations_db": "question",
        "query_fleet_database": "question",
        "check_task_status": "item='all'",
        "check_equipment_status": "equipment='all'",
        "check_suit_status": "suit='all'",
        "schedule_personal_event": "event, when='unspecified time'",
        "schedule_operation": "operation, when='as ordered'",
        "schedule_reminder": "text, when='unspecified time'",
        "remember_preference": "key, value",
        "send_alert": "message",
        "lookup_knowledge_base": "query",
        "view_action_log": "",
        "remember_fact": "key, value",
        "recall_fact": "key",
    }
    return hints.get(name, "")


def run_tool(name, **kwargs):
    if name not in TOOL_REGISTRY:
        return f"ERROR: no such tool '{name}'. Available tools: {', '.join(TOOL_REGISTRY.keys())}"
    return TOOL_REGISTRY[name]["fn"](**kwargs)

