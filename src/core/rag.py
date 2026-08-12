"""
src/core/rag.py - the RAG pipeline: Retrieval & Context Injection, then Generation & Formatting.

This module ONLY answers questions using retrieved context - it never takes an action.
That's the deliberate RAG-vs-Agentic distinction the course teaches.
"""

from src.core.vector_store import retrieve
from src.core.llm import chat
from config.settings import settings

CHITTI_SYSTEM_PROMPT = settings.CHITTI_SYSTEM_PROMPT
TOP_K = settings.TOP_K

# Keywords that signal the user is asking about CHITTI's own identity (the AI robot),
# NOT about the human user. These bypass RAG so the context never overrides identity.
_SELF_IDENTITY_KEYWORDS = [
    "your name", "who are you", "what are you", "your identity",
    "introduce yourself", "tell me about yourself",
]

# Keywords that signal the user is asking about THEIR OWN identity.
_USER_IDENTITY_KEYWORDS = [
    "my name", "who am i", "what is my name", "what's my name",
]


def _is_self_identity_question(query: str) -> bool:
    q = query.lower().strip()
    return any(kw in q for kw in _SELF_IDENTITY_KEYWORDS)


def _is_user_identity_question(query: str) -> bool:
    q = query.lower().strip()
    return any(kw in q for kw in _USER_IDENTITY_KEYWORDS)


def format_context(chunks):
    """Context injection: format retrieved chunks with clear source labels, so the model
    can (and must) cite which knowledge type answered - and so we avoid the classic
    'dump everything in, hope for the best' mistake from the course."""
    if not chunks:
        return "Boss, this information is not in CHITTI's database."
    lines = []
    for i, c in enumerate(chunks, 1):
        lines.append(f"[{i}] (source: {c['doc_type']}) {c['text']}")
    return "\n".join(lines)


def answer(query, top_k=TOP_K, history=None):
    """Retrieval & Context Injection -> Generation & Formatting. Returns the reply text
    and the retrieved chunks (so the caller/demo can show what was retrieved)."""

    # --- Identity short-circuit: answer without RAG context ---
    # "What is your name?" -> CHITTI is the AI agent, not Gokul.
    if _is_self_identity_question(query):
        messages = [{"role": "system", "content": CHITTI_SYSTEM_PROMPT}]
        if history:
            messages.extend(history)
        messages.append({
            "role": "user",
            "content": (
                "QUESTION: " + query + "\n\n"
                "Answer strictly from your IDENTITY rules above. "
                "Do NOT use any retrieved context. "
                "State your own name (CHITTI, the AI robot) clearly."
            ),
        })
        reply = chat(messages)
        return reply, []

    # "What is my name?" -> answer about Gokul from the system prompt identity rules.
    if _is_user_identity_question(query):
        messages = [{"role": "system", "content": CHITTI_SYSTEM_PROMPT}]
        if history:
            messages.extend(history)
        messages.append({
            "role": "user",
            "content": (
                "QUESTION: " + query + "\n\n"
                "Answer strictly from your IDENTITY rules above. "
                "State the master's name (Gokul) clearly."
            ),
        })
        reply = chat(messages)
        return reply, []

    # --- Normal RAG path ---
    chunks = retrieve(query, top_k=top_k)
    context = format_context(chunks)

    messages = [{"role": "system", "content": CHITTI_SYSTEM_PROMPT}]
    if history:
        messages.extend(history)
    messages.append({
        "role": "user",
        "content": f"CONTEXT:\n{context}\n\nQUESTION: {query}\n\nAnswer using ONLY the context above.",
    })

    reply = chat(messages)
    return reply, chunks
