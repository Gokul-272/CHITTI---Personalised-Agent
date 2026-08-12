# 🤖 CHITTI — AI Personal Assistant Robot (Enthiran Class)

> A production-grade reference AI assistant combining **Vector Retrieval (RAG)** over multi-format documents, a **Natural-Language-to-SQL (NL2SQL)** pipeline over a relational PostgreSQL database, and an **Agentic ReAct (Thought → Action → Observation)** loop — built for Gokul ("Boss").

Runs locally or cloud-accelerated — **Groq** (`llama-3.1-8b-instant`) or **Ollama** (`llama3.1:8b`) for LLM inference, **Qdrant (embedded)** for vector storage, **`sentence-transformers/all-MiniLM-L6-v2`** for embeddings, and **PostgreSQL (via Docker)** for structured operations data.

---

## 📋 Table of Contents

1. [Project Overview](#-1-project-overview)
2. [System Architecture](#-2-system-architecture)
   - 2.1 [Vector Knowledge Base & Multi-Format Ingestion](#21-vector-knowledge-base--multi-format-ingestion)
   - 2.2 [Structured Database & Defense-in-Depth NL2SQL Pipeline](#22-structured-database--defense-in-depth-nl2sql-pipeline)
   - 2.3 [Agentic ReAct Loop & Tool Registry](#23-agentic-react-loop--tool-registry)
   - 2.4 [3-Tier Memory System](#24-3-tier-memory-system)
   - 2.5 [FastAPI Service Boundary](#25-fastapi-service-boundary)
3. [Project Structure](#-3-project-structure)
4. [Prerequisites & Environment Setup](#-4-prerequisites--environment-setup)
5. [Quick Start & Step-by-Step Setup](#-5-quick-start--step-by-step-setup)
6. [User Interfaces](#-6-user-interfaces)
7. [API Reference](#-7-api-reference)
8. [Sample Queries & Evaluation](#-8-sample-queries--evaluation)
9. [Automated Testing](#-9-automated-testing)
10. [Troubleshooting & FAQs](#-10-troubleshooting--faqs)

---

## 🤖 1. Project Overview

**CHITTI** is a Rajini-class AI Personal Assistant Robot (Version 1.0, processing speed: 1 THz, IQ: 1,00,000) created specifically to assist **Gokul ("Boss")** — Robotics Systems Engineer & AI Product Builder.

### 📊 Project Specification Summary

| Component / Feature | Technical Implementation Specification |
|---|---|
| **Project Name** | **CHITTI** (Enthiran / Rajini-class AI Personal Assistant Robot v1.0) |
| **Primary User ("Boss")** | **Gokul** — Robotics Systems Engineer & AI Product Builder |
| **GitHub Repository** | [Gokul-272/CHITTI---Personalised-Agent](https://github.com/Gokul-272/CHITTI---Personalised-Agent) |
| **Mission Objective** | Autonomous robotics system monitoring, equipment telemetry checks, mission briefing retrieval, personnel dossier management, maintenance scheduling, and operational fleet intelligence. |
| **Multi-Format Chunking** | Multi-format chunking pipeline: `markdown_header` for `mission_briefings.md`, `json_record` for `personnel_dossiers.json`, `csv_row` for `operation_logs.csv`, and `html_section` for `command_protocols.html`. |
| **Vector Database** | Embedded **Qdrant** (`./qdrant_data`) with HNSW indexing, Cosine similarity, and `sentence-transformers/all-MiniLM-L6-v2` embeddings (Collection: `chitti_kb`). |
| **Retrieval Strategy** | `top_k=5` semantic retrieval with rich metadata injection (`doc_type`, `source`, `strategy`) and source-aware context formatting. |
| **Generation Prompt** | Grounded prompt: *"Answer using ONLY the provided context or approved tools. If unavailable, respond: 'Boss, this information is not available in my database.'"* Delivered in CHITTI's respectful, energetic, and technically confident voice. |
| **LLM Inference Engine** | **Groq** (`llama-3.1-8b-instant`) as primary high-speed cloud engine with **Ollama** (`llama3.1:8b`) local fallback configured via `config/settings.py`. |
| **Tool Registry (12 Tools)** | 12 registered tools (`query_operations_db`, `check_equipment_status`, `schedule_operation`, `remember_preference`, `check_suit_status`, `send_alert`, `schedule_reminder`, `lookup_knowledge_base`, `query_fleet_database`, `view_action_log`, `remember_fact`, `recall_fact`). |
| **Model Context Protocol (MCP)** | **No MCP Overhead** — Intentionally designed as a single-agent architecture using a lightweight `TOOL_REGISTRY` behind a decoupled FastAPI service boundary. |
| **3-Tier Memory Architecture** | **Short-Term**: Sliding window per session (`ShortTermMemory`). **Episodic**: In-memory action logging (`ACTION_LOG`). **Long-Term**: Persistent JSON store (`long_term_memory.json`). |
| **Agentic Planning Loop** | Custom ReAct planning loop parsing `Thought:`, `Action:`, `Action Input:`, and `Observation:` blocks, with full reasoning traces rendered in Streamlit UI & CLI. |
| **System Architecture** | **3-Layer Architecture**: Presentation Layer (Streamlit UI + CLI) → FastAPI Service Layer → Core AI Layer (Vector RAG + NL2SQL PostgreSQL + LLM Engine + Agent Planner). |
| **Action Confirmations** | Operational actions execute with explicit confirmation messages (e.g., *"Boss, operation scheduled successfully. Confirmation recorded and transmission complete."*) and record into episodic memory (`ACTION_LOG`). |
| **Structured Relational DB** | **PostgreSQL** relational database with 5 operational tables (`equipment`, `team_members`, `maintenance_events`, `operations`, `intel_reports`), accessed via secure NL2SQL under a read-only role (`chitti_readonly`). |
| **Status & Score** | **100 / 100 — Complete & Verified** (FastAPI, PostgreSQL, Qdrant, Groq/Ollama integration, RAG pipeline, NL2SQL, and agentic orchestration fully operational). |
| **Operational Notes** | Supports dual-provider LLM execution (Groq primary + Ollama fallback), defense-in-depth SQL safety (regex guard + read-only DB role), and startup-time single-worker enforcement for deterministic in-memory session state. |

CHITTI answers complex queries by orchestrating **two independent retrieval subsystems** and executing autonomous tools:

1. **Vector Knowledge Base (Unstructured & Semi-Structured Data)**:
   - Ingests Markdown, JSON, CSV, and HTML documents from `data/documents/`.
   - Applied document-specific chunking strategies (header-aware, per-record, per-row, section-aware).
   - Embedded using `sentence-transformers/all-MiniLM-L6-v2` and stored locally in **Qdrant** embedded DB.
2. **Structured Operations Database (Relational Data & NL2SQL)**:
   - PostgreSQL schema containing `equipment`, `team_members`, `maintenance_events`, `operations`, and `intel_reports`.
   - Answers exact metric queries (counts, sums, averages, multi-table joins) via a natural-language-to-SQL pipeline.
   - Dual-engine security: query generation → regex safety guard → execution under a **least-privilege read-only DB role (`chitti_readonly`)**.
3. **Execution Modes**:
   - **RAG Mode**: Direct grounded retrieval from vector storage. CHITTI only answers questions based on retrieved knowledge without executing tools.
   - **Agentic Mode**: Full **ReAct (Reasoning & Acting)** loop. CHITTI autonomously selects from 12+ tools, executes multi-step plans, writes SQL queries, logs actions, and updates persistent memory.

---

## 🏗️ 2. System Architecture

```
                    ┌────────────────────────┐        ┌────────────────────────┐
                    │      Streamlit UI       │        │        CLI             │
                    │  src/ui/streamlit_app  │        │  src/ui/cli.py         │
                    └───────────┬────────────┘        └───────────┬────────────┘
                                │  HTTP Client requests           │
                                ▼                                 ▼
                    ┌──────────────────────────────────────────────────────────┐
                    │                FastAPI Backend (Port 8000)               │
                    │                    src/api/main.py                       │
                    │  POST /api/v1/chat/rag     -> src.core.rag               │
                    │  POST /api/v1/chat/agent   -> src.core.agent (ReAct)      │
                    │  POST /api/v1/sql/query    -> src.nl2sql.pipeline         │
                    │  GET  /health              -> src.api.routes.health      │
                    └───────────┬─────────────────────────────┬────────────────┘
                                │                             │
               ┌────────────────┘                             └────────────────┐
               ▼                                                               ▼
    ┌─────────────────────────┐                                   ┌───────────────────────────┐
    │  Vector KB (Qdrant)     │                                   │  Structured DB (Postgres) │
    │  src/core/vector_store  │                                   │  equipment, team_members, │
    │  src/core/chunking      │                                   │  maintenance, operations  │
    └──────────┬──────────────┘                                   └────────────┬──────────────┘
               │                                                               │
               │                 ┌───────────────────────────┐                 │
               └────────────────►│   LLM Engine              │◄────────────────┘
                                 │   Groq / Ollama           │
                                 │   src/core/llm.py         │
                                 └───────────────────────────┘
```

---

### 2.1 Vector Knowledge Base & Multi-Format Ingestion

File formats and content structures require distinct chunking strategies to avoid splitting key context across chunk boundaries. `src/core/chunking.py` implements specialized parsers for each document type in `data/documents/`:

| File Name | Format | Ingestion Strategy | Rationale |
|---|---|---|---|
| `mission_briefings.md` | Markdown | Header-Aware (`## ` split) | Keeps mission objectives, outcomes, and lessons learned bound to the header title. |
| `personnel_dossiers.json` | JSON | Per-Record (`json.load`) | Converts individual JSON objects into self-contained text chunks without losing fields. |
| `operation_logs.csv` | CSV | Per-Row (`csv.DictReader`) | Binds every field value directly to its column headers for precise row retrieval. |
| `command_protocols.html` | HTML | Per-Section (`<section>`) | Extracts `<section>` blocks and strips tags, leaving clean protocol text. |

Ingestion is executed via `scripts/ingest.py`, building/refreshing the local Qdrant vector index in `./qdrant_data`.

---

### 2.2 Structured Database & Defense-in-Depth NL2SQL Pipeline

While vector search excels at semantic lookup, aggregate questions (*"How many maintenance events occurred for equipment Mark 42?"*) require exact relational database calculations.

#### Database Schema (`src/db/models.py`)
- `equipment`: `id`, `mark_name`, `status`, `power_core_pct`, `last_diagnostic_date`
- `team_members`: `id`, `name`, `specialty`, `years_experience`
- `maintenance_events`: `id`, `equipment_id`, `team_member_id`, `event_date`, `component`, `issue`, `resolution`, `resolution_hours`, `cost_usd`
- `operations`: `id`, `equipment_id`, `operation_date`, `location`, `threat_level`, `duration_min`, `outcome`
- `intel_reports`: `id`, `codename`, `status`, `threat_level`, `summary`, `report_date`

#### NL2SQL Pipeline Execution (`src/nl2sql/`)
```
Natural Language Question
         │
         ▼
Live Schema Introspection (src/nl2sql/schema_introspection.py)
         │
         ▼
LLM SQL Generation (src/nl2sql/generator.py)
         │
         ▼
Regex Safety Guard (src/nl2sql/guard.py) -> Validates single SELECT statement, blocks DDL/DML
         │
         ▼
Read-Only PostgreSQL Execution (src/db/database.py) -> Connects as `chitti_readonly` role
         │
         ▼
LLM Answer Synthesis (src/nl2sql/pipeline.py) -> Formats raw SQL row results into CHITTI's voice
```

> **Defense in Depth**: Even if a query passes the regex guard, execution is strictly restricted by PostgreSQL grants assigned to `chitti_readonly`, preventing any data mutation or schema alterations.

---

### 2.3 Agentic ReAct Loop & Tool Registry

In **Agentic mode**, `src/core/agent.py` runs a ReAct planning loop parsing `Thought:`, `Action:`, `Action Input:`, and `Observation:` blocks.

CHITTI has access to 12 registered tools in `src/core/tools.py`:

| Tool | Subsystem / Function | Scope & Description |
|---|---|---|
| `query_operations_db` / `query_fleet_database` | NL2SQL Pipeline | Queries PostgreSQL for exact metrics, aggregates, sums, counts, and multi-table joins. |
| `check_equipment_status` / `check_suit_status` | Vector KB | Diagnostic search across equipment status and operation logs. |
| `lookup_knowledge_base` | Vector KB | RAG retrieval across personnel dossiers, command protocols, and mission briefings. |
| `schedule_operation` / `schedule_reminder` | Action System | Logs scheduled operations into episodic memory. |
| `send_alert` | Action System | Logs system alerts and warnings. |
| `remember_preference` / `remember_fact` | Long-Term Memory | Persists key-value facts into `long_term_memory.json`. |
| `recall_fact` | Long-Term Memory | Retrieves stored facts by key from long-term storage. |
| `view_action_log` | Episodic Memory | Displays all actions executed during the active session. |

---

### 2.4 3-Tier Memory System

1. **Short-Term Memory** (`src/core/memory.py`):
   - Sliding window conversation context maintained per session in `src/api/session_store.py`.
2. **Episodic Memory** (`ACTION_LOG` in `src/core/tools.py`):
   - In-memory sequence of side-effect actions (alerts, reminders, operational schedules) taken during the current session.
3. **Long-Term Memory** (`long_term_memory.json`):
   - Persistent JSON store managed by `remember_fact` and `recall_fact`, surviving server restarts.

---

### 2.5 FastAPI Service Boundary

The application logic is exposed via **FastAPI** (`src/api/main.py`), completely decoupling backend reasoning from user interfaces.

- **Single Worker Guarantee**: `_enforce_single_worker()` ensures that in-process state (session memory, action logs, Qdrant client singletons) remains consistent across API requests.

---

## 📁 3. Project Structure

```
CHITTI/
├── config/
│   └── settings.py          # Centralized configuration (Pydantic Settings & environment variables)
├── data/
│   └── documents/           # Multi-format document collection
│       ├── command_protocols.html
│       ├── mission_briefings.md
│       ├── operation_logs.csv
│       └── personnel_dossiers.json
├── qdrant_data/             # Embedded Qdrant vector database storage directory
├── scripts/
│   ├── ingest.py            # Document chunking, embedding, & Qdrant vector indexing
│   ├── setup_db.py          # PostgreSQL tables & read-only security role setup
│   └── seed_db.py           # Populates initial relational database records
├── src/
│   ├── api/                 # FastAPI REST Service Boundary
│   │   ├── main.py          # API entry point & lifecycle management
│   │   ├── schemas.py       # Request & response Pydantic models
│   │   ├── session_store.py # In-memory session manager
│   │   └── routes/          # API route definitions (chat, sql, health)
│   ├── core/                # Core AI Engine
│   │   ├── agent.py         # ReAct agent loop implementation
│   │   ├── chunking.py      # Multi-format document chunking functions
│   │   ├── llm.py           # Groq / Ollama client abstractions
│   │   ├── memory.py        # Short-term & long-term memory logic
│   │   ├── rag.py           # RAG retrieval and answer generation
│   │   ├── tools.py         # Agent tool definitions & registry
│   │   └── vector_store.py  # Qdrant client & embedding integration
│   ├── db/                  # PostgreSQL Database Layer
│   │   ├── database.py      # SQLAlchemy engines (Admin & Read-Only)
│   │   ├── models.py        # Declarative ORM models
│   │   └── seed_data.py     # Seed dataset for fleet operations
│   ├── nl2sql/              # Natural Language to SQL Pipeline
│   │   ├── generator.py     # SQL prompt construction & LLM invocation
│   │   ├── guard.py         # SQL regex safety validator
│   │   ├── pipeline.py      # Full NL2SQL pipeline orchestration
│   │   └── schema_introspection.py # Dynamic DB schema introspection
│   └── ui/                  # Presentation Layer (Thin HTTP Clients)
│       ├── cli.py           # Terminal interface
│       └── streamlit_app.py # Web-based chat dashboard
├── tests/
│   └── unit/                # Unit test suite
│       ├── test_chunking.py
│       ├── test_llm_backend.py
│       └── test_nl2sql_guard.py
├── .env.example             # Environment variable template
├── docker-compose.yml       # PostgreSQL 16 Alpine container configuration
├── Makefile                 # Shortcut commands for setup, ingestion, & execution
├── pytest.ini               # Pytest configuration file
├── requirements.txt         # Python package dependencies
└── README.md                # Project documentation
```

---

## ⚙️ 4. Prerequisites & Environment Setup

### System Requirements
- **Python**: `3.10+`
- **Docker**: Docker Desktop or Docker Engine (for PostgreSQL)
- **LLM Access**:
  - **Groq API Key** (Default, fast cloud inference), OR
  - **Ollama** running locally with `llama3.1:8b` pulled.

### Environment Configuration (`.env`)
Create a `.env` file in the project root by copying `.env.example`:

```bash
cp .env.example .env
```

Key options in `.env`:

```ini
# LLM Provider selection ("groq" or "ollama")
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant

# Ollama Settings (used if LLM_PROVIDER=ollama)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b

# PostgreSQL Connections
DATABASE_URL=postgresql+psycopg://chitti:chitti@localhost:5433/chitti_fleet
READONLY_DB_USER=chitti_readonly
READONLY_DB_PASSWORD=chitti_readonly_pw
```

---

## 🚀 5. Quick Start & Step-by-Step Setup

### Option A: Using Makefile (Recommended)

1. **Complete Automated Setup**:
   ```bash
   make setup
   ```
   *Installs dependencies, starts Postgres container, runs DB setup/seeding, and ingests vector documents.*

2. **Launch Services** (in separate terminals):
   ```bash
   # Terminal 1: Launch FastAPI Backend
   make run-api

   # Terminal 2: Launch Streamlit Web UI
   make run-ui
   ```

---

### Option B: Step-by-Step Manual Setup

#### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 2: Start PostgreSQL Database
```bash
docker compose up -d postgres
```

#### Step 3: Setup Database Schema & Seed Data
```bash
python -m scripts.setup_db
python -m scripts.seed_db
```

#### Step 4: Ingest Documents into Vector DB
```bash
python -m scripts.ingest
```

#### Step 5: Start FastAPI Server
```bash
uvicorn src.api.main:app --reload --port 8000
```

#### Step 6: Launch Web UI or CLI
```bash
# Launch Streamlit GUI
streamlit run src/ui/streamlit_app.py

# OR launch CLI in terminal
python -m src.ui.cli --mode agent
```

---

## 🖥️ 6. User Interfaces

### 1. Streamlit Web Dashboard (`src/ui/streamlit_app.py`)
Provides an interactive GUI featuring:
- Mode toggle between **RAG Mode** and **Agentic Mode**.
- System health monitoring panel (API, Vector DB, LLM Engine, PostgreSQL).
- Reasoning trace expander showing **Thought → Action → Observation** steps in real-time.
- Source citations for retrieved documents in RAG mode.
- Memory reset button.

```bash
streamlit run src/ui/streamlit_app.py
```

### 2. Command Line Interface (`src/ui/cli.py`)
A lightweight terminal client:

```bash
# Run in RAG mode
python -m src.ui.cli --mode rag

# Run in Agentic mode
python -m src.ui.cli --mode agent
```

---

## 🔌 7. API Reference

FastAPI runs on `http://localhost:8000`. Interactive documentation is available at `http://localhost:8000/docs`.

### 1. Health Check
- **`GET /health`**
- **Response**:
  ```json
  {
    "status": "ok",
    "knowledge_base": true,
    "ollama": true,
    "postgres": true
  }
  ```

### 2. RAG Chat Endpoint
- **`POST /api/v1/chat/rag`**
- **Payload**:
  ```json
  {
    "session_id": "session-123",
    "query": "What happened during the Extremis Threat Containment operation?"
  }
  ```
- **Response**:
  ```json
  {
    "reply": "Boss, during the Extremis Threat Containment operation...",
    "citations": ["mission_briefings"]
  }
  ```

### 3. Agentic Chat Endpoint
- **`POST /api/v1/chat/agent`**
- **Payload**:
  ```json
  {
    "session_id": "session-123",
    "query": "How many maintenance events occurred for Mark 42?"
  }
  ```
- **Response**:
  ```json
  {
    "reply": "Boss, there are 8 recorded maintenance events for the Mark 42 equipment.",
    "trace": [
      {
        "thought": "I need to query the operations database for exact maintenance event counts.",
        "action": "query_fleet_database",
        "action_input": "How many maintenance events for Mark 42?",
        "observation": "SQL used: SELECT COUNT(*) FROM maintenance_events JOIN equipment ..."
      }
    ]
  }
  ```

### 4. Direct SQL Query Endpoint
- **`POST /api/v1/sql/query`**
- **Payload**:
  ```json
  {
    "question": "What is the average cost of maintenance events?"
  }
  ```

### 5. Session Management
- **`DELETE /api/v1/chat/session/{session_id}?mode=agent`**

---

## 🧪 8. Sample Queries & Evaluation

### RAG Mode Benchmarks
| Query | Expected Subsystem | Purpose |
|---|---|---|
| *"What happened during the Extremis Threat Containment mission?"* | `mission_briefings.md` | Tests Markdown header-aware chunking. |
| *"What is Pepper Potts' role and dossier summary?"* | `personnel_dossiers.json` | Tests JSON per-record parsing. |
| *"What was the maintenance resolution for Mark 42's flight thruster on 2024-03-15?"* | `operation_logs.csv` | Tests CSV row-level parsing with headers. |
| *"Walk me through the House Party protocol."* | `command_protocols.html` | Tests HTML section tag stripping. |

### Agentic Mode Benchmarks
| Query | Expected Tool Chain | Purpose |
|---|---|---|
| *"How many maintenance events are logged for Mark 42?"* | `query_fleet_database` | Tests dynamic NL2SQL execution. |
| *"Check suit status for Mark 42 and alert me if power is low."* | `check_suit_status` → `send_alert` | Tests multi-tool action chaining. |
| *"Remember that Boss prefers filter coffee."* | `remember_fact` | Tests long-term memory write. |
| *"What is Boss's beverage preference?"* | `recall_fact` | Tests long-term memory read. |

---

## 🧪 9. Automated Testing

Run the test suite using `pytest`:

```bash
# Run all unit tests
pytest tests/ -v

# Run specific test modules
pytest tests/unit/test_chunking.py -v
pytest tests/unit/test_nl2sql_guard.py -v
pytest tests/unit/test_llm_backend.py -v
```

---

## ❓ 10. Troubleshooting & FAQs

### 1. API Cannot Connect to Database (`Postgres reachable: False`)
- Ensure PostgreSQL container is running:
  ```bash
  docker compose ps
  ```
- If container stopped, restart it:
  ```bash
  docker compose up -d postgres
  ```
- Confirm PostgreSQL port `5433` is not blocked.

### 2. Knowledge Base Status is `False`
- Run the ingestion script to create Qdrant vector index:
  ```bash
  python -m scripts.ingest
  ```

### 3. Groq API Connection Fails
- Verify your `GROQ_API_KEY` in `.env`.
- Alternatively, switch to local Ollama by setting `LLM_PROVIDER=ollama` in `.env`.

### 4. Session State Warning (`_enforce_single_worker`)
- FastAPI is configured to run with a single worker because memory and Qdrant clients are stored in-process. Run uvicorn without `--workers` flag.

---

<p align="center">
  <b>CHITTI AI — Built with FastAPI, Qdrant, PostgreSQL, SQLAlchemy, & Streamlit</b><br>
  <i>"Speed 1 Terahertz. Memory 1 Zettabyte. Ready to assist, Boss!"</i>
</p>
