from config.settings import settings
from src.core.tools import TOOL_REGISTRY


def test_llm_defaults_are_configured_for_groq_and_chitti():
    assert hasattr(settings, "LLM_PROVIDER")
    assert settings.LLM_PROVIDER in {"groq", "ollama"}
    assert settings.GROQ_MODEL == "llama-3.1-8b-instant"
    assert "CHITTI" in settings.CHITTI_SYSTEM_PROMPT.upper()


def test_goat_tool_registry_has_operations_specific_tools():
    expected = {"query_operations_db", "check_equipment_status", "schedule_operation", "remember_preference"}
    assert expected.issubset(TOOL_REGISTRY.keys())
