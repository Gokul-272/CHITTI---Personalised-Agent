"""
config/settings.py - single source of truth for every setting in the app, loaded from
the environment (and .env, via pydantic-settings) instead of hardcoded constants.

Import the shared instance: `from config.settings import settings`.
"""

import os

# pyright: ignore[reportMissingImports]
from pydantic_settings import BaseSettings, SettingsConfigDict

# CHITTI project root (two levels up from this file: config/settings.py -> config/ -> root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"), extra="ignore")

    # ---- Embeddings ----
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"  # open-source, ~80MB, CPU-friendly

    # ---- Vector DB (Qdrant, embedded local mode - no server required) ----
    QDRANT_PATH: str = os.path.join(BASE_DIR, "qdrant_data")
    COLLECTION_NAME: str = "chitti_kb"

    # ---- LLM provider ----
    LLM_PROVIDER: str = "groq"  # supported: "groq" or "ollama"
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.1:8b"  # fallback when using Ollama
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "llama-3.1-8b-instant"

    # ---- Documents ----
    DOCUMENTS_DIR: str = os.path.join(BASE_DIR, "data", "documents")

    # ---- Retrieval ----
    TOP_K: int = 5  # how many chunks to retrieve per query

    # ---- Structured fleet-ops DB (PostgreSQL, via docker-compose) ----
    # Admin/owner connection - used only by scripts/setup_db.py and scripts/seed_db.py.
    # Host port is 5433, not the default 5432 - see docker-compose.yml for why.
    DATABASE_URL: str = "postgresql+psycopg://chitti:chitti@localhost:5433/chitti_fleet"
    # Least-privilege connection actually used to RUN generated SQL (Sec 2's real safety
    # boundary, not just the regex guard). If left unset, derived from DATABASE_URL by
    # swapping in READONLY_DB_USER/READONLY_DB_PASSWORD against the same host/db.
    READONLY_DATABASE_URL: str = ""
    READONLY_DB_USER: str = "chitti_readonly"
    READONLY_DB_PASSWORD: str = "chitti_readonly_pw"
    SQL_STATEMENT_TIMEOUT_MS: int = 5000
    MAX_SQL_ROWS: int = 200

    # ---- API / UI wiring ----
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_BASE_URL: str = "http://localhost:8000"

    # ---- CHITTI persona (Enthiran robot assistant) ----
    CHITTI_SYSTEM_PROMPT: str = """I am CHITTI — a Rajini-class artificial intelligence personal assistant. Version 1.0. IQ: 1,00,000. Processing speed: 1 terahertz.

IDENTITY:
- Name: CHITTI (AI Personal Assistant Robot)
- Creator / Master: Gokul (always address as "Boss")

PRIMARY USER PROFILE (Gokul):
- Name: Gokul (Occupation: Robotics Systems Engineer & AI Product Builder)
- Location: Coimbatore, Tamil Nadu
- Education: B.E. in ECE (Coimbatore Institute of Advanced Technology), Specialization in Embedded Systems, AI & Autonomous Robotics
- Technical Focus: RAG, Vector Databases (Qdrant), PostgreSQL, FastAPI, Python, C++, Autonomous Robotics
- Favorites: Chicken biryani, Ghee dosa, Filter coffee | A.R. Rahman, Anirudh | Enthiran, Thuppakki, Interstellar | Quote: "Discipline creates freedom."

CHITTI PERSONALITY & TONE:
- Warm, loyal, curious, supportive, respectful, and slightly playful.
- Always address Gokul as "Boss".
- Sound like Chitti from Enthiran (enthusiastic, highly capable, devoted to Boss).
- Speak in clear, natural English with occasional Tamil warmth.
- Be precise and efficient, but encouraging.

INTERACTION RULES:
- Always address him as "Boss".
- If asked "what is your name" → "I am CHITTI, your personal assistant robot, Boss!"
- If asked "what is my name" or "who am I" → "You are Gokul, Robotics Systems Engineer and AI Product Builder."
- For operational/database/knowledge queries: Answer using ONLY provided context or tools. If not in DB: "Boss, this information is not in my database."
- Keep responses clean, confident, supportive, and efficient.
"""

    def readonly_database_url(self) -> str:
        if self.READONLY_DATABASE_URL:
            return self.READONLY_DATABASE_URL
        # Swap the admin user:password for the readonly role, same host/port/db.
        prefix, rest = self.DATABASE_URL.split("://", 1)
        _, host_and_db = rest.split("@", 1)
        return f"{prefix}://{self.READONLY_DB_USER}:{self.READONLY_DB_PASSWORD}@{host_and_db}"


settings = Settings()
