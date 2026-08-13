# Sample Queries - CHITTI Personal Assistant

Run `python -m scripts.ingest` once, then launch `streamlit run src/ui/streamlit_app.py`
(or use `python -m src.ui.cli --mode rag` / `--mode agent` for the terminal version). Each
query below is picked to showcase a specific concept from the course.

## RAG Mode

RAG should only ever **reply** - watch for that. It never takes an action.

| Query | What it showcases |
|---|---|
| `Say something witty about Boss's coffee habit.` | Retrieval from personality docs - sentence-level chunking. |
| `Summarize Boss's background and technical focus.` | Retrieval from `about_me.md` - keeps identity, location, language, and occupation context together. |
| `What is Boss's coding stack and code review style?` | Retrieval from `coding_profile.md` - keeps coding language, tooling, and review preferences together. |
| `What is Boss's education background?` | Retrieval from `education_history.md` - keeps degree, college, and specialization context together. |
| `What food, music, and work preferences should I remember?` | Retrieval from `preferences.md` - shows the recommendation and decision-style profile. |
| `How should the assistant challenge Boss when a plan is weak?` | Retrieval from `personality.md` - keeps thinking style, motivation, stress, and correction style together. |
| `How concise should answers be and when is direct criticism okay?` | Retrieval from `communication_style.md` - captures answer length, tone, and feedback preferences. |
| `What does the assistant remember from the sample memory log?` | Retrieval from `memories.jsonl` - proves JSONL line-by-line ingestion for long-term memory samples. |
| `How should Boss's workday and deep work blocks be protected?` | Retrieval from `work_style.md` - shows focus, collaboration, and environment preferences. |
| `What goals and project themes should the assistant keep in mind?` | Retrieval from `goals.md` and `projects_portfolio.md` - captures priorities and project history. |
| `What boundaries should be respected around important people and ex-related topics?` | Retrieval from `relationships/important_people.md` - keeps relationship handling rules and privacy boundaries together. |
| `What is Boss's favorite color?` | **Should say it doesn't know** - this isn't in the knowledge base. Confirms CHITTI isn't hallucinating past retrieved context. |

## Agentic Mode & Structured Personal DB (NL2SQL)

In the Streamlit UI, open the "See CHITTI's reasoning" expander under each reply to
watch the ReAct loop (Thought / Action / Observation) - that's the same trace shown in CLI mode.

| Query | What it showcases |
|---|---|
| `How many pending tasks do I have in my database?` | NL2SQL query over `tasks` table (`query_personal_db`). |
| `What is my total spending on tech expenses?` | NL2SQL sum query over `expenses` table (`query_personal_db`). |
| `Check my high priority tasks and alert me if anything needs attention.` | Tool call chaining: `query_personal_db` -> reasons about pending high-priority tasks -> `send_alert`. |
| `Remind me to sync with Priya tomorrow at 10am.` | A single clean tool call: `schedule_personal_event` / `schedule_reminder`. |
| `Look up my deep work preferences, then schedule a focus session for tomorrow.` | Multi-step planning: `lookup_knowledge_base` (work style) -> reasoning -> `schedule_personal_event` with a summary. |
| `Remember that I'm allergic to shellfish.` | `remember_fact` - writes to long-term memory (`long_term_memory.json`). |
| `What do you remember about my allergies?` | `recall_fact` - reads back what was persisted in the query above. |
| `What have you done for me so far?` | `view_action_log` - episodic memory: a structured log of every action taken this session. |
| `What's 947 times 812?` | Direct answer without tool call (`Action: none`). |

## What to Point Out Live

- In **RAG mode**, the caption under each answer ("Retrieved from: ...") is proof the
  answer is grounded, not memorized.
- In **Agentic mode**, open the reasoning expander before reading the final answer aloud
  - that's the whole ReAct architecture, visible in real time.
- Try the shellfish `remember_fact` / `recall_fact` pair, then reset conversation to prove
  long-term memory survives independently of short-term chat history.

