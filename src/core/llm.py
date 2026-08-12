"""src/core/llm.py - small provider wrapper for Groq or Ollama."""

import requests
from groq import Groq

from config.settings import settings

LLM_PROVIDER = settings.LLM_PROVIDER
OLLAMA_HOST = settings.OLLAMA_HOST
OLLAMA_MODEL = settings.OLLAMA_MODEL
GROQ_API_KEY = settings.GROQ_API_KEY
GROQ_MODEL = settings.GROQ_MODEL


class LLMUnavailable(RuntimeError):
    pass


class OllamaUnavailable(LLMUnavailable):
    pass


class GroqUnavailable(LLMUnavailable):
    pass


def chat(messages, temperature=0.4, model=None):
    """Send a chat completion through the active provider."""
    if LLM_PROVIDER == "groq":
        return _chat_via_groq(messages, temperature=temperature, model=model)
    return _chat_via_ollama(messages, temperature=temperature, model=model)


def _chat_via_groq(messages, temperature=0.4, model=None):
    model = model or GROQ_MODEL
    if not GROQ_API_KEY:
        raise GroqUnavailable("GROQ_API_KEY is not set. Add your Groq key to .env before using CHITTI.")
    try:
        client = Groq(api_key=GROQ_API_KEY)
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return resp.choices[0].message.content
    except Exception as exc:  # pragma: no cover - network/provider failure path
        raise GroqUnavailable(f"Groq call failed: {exc}") from exc


def _chat_via_ollama(messages, temperature=0.4, model=None):
    """messages: list of {"role": "system"|"user"|"assistant", "content": str}
    Returns the assistant's reply text. Raises OllamaUnavailable with a friendly
    message if Ollama isn't running or the model isn't pulled."""
    model = model or OLLAMA_MODEL
    try:
        resp = requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={"model": model, "messages": messages, "stream": False, "options": {"temperature": temperature}},
            timeout=120,
        )
    except requests.exceptions.ConnectionError:
        raise OllamaUnavailable(
            "Could not reach Ollama at " + OLLAMA_HOST + ".\n"
            "Is Ollama installed and running? See README.md 'Setup' section.\n"
            "Quick check: run `ollama list` in a terminal - if that fails, start Ollama first."
        )

    if resp.status_code == 404:
        raise OllamaUnavailable(
            f"Ollama is running, but the model '{model}' isn't pulled yet.\n"
            f"Run: ollama pull {model}"
        )
    resp.raise_for_status()
    data = resp.json()
    return data["message"]["content"]


def llm_alive():
    """Best-effort health check used by the Streamlit sidebar."""
    if LLM_PROVIDER == "groq":
        return bool(GROQ_API_KEY)
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def ollama_alive():
    return llm_alive() if LLM_PROVIDER != "ollama" else llm_alive()
