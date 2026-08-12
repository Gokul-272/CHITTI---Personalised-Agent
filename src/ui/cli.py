"""
src/ui/cli.py - command-line entry point for the CHITTI demo (the Streamlit app in
streamlit_app.py is the primary interface - this CLI is kept for quick terminal testing).

A THIN HTTP CLIENT of src/api, same as the Streamlit app - run the API first:
    uvicorn src.api.main:app --reload --port 8000

Usage (from the project root):
    python -m src.ui.cli --mode rag      # RAG only - CHITTI replies, never acts
    python -m src.ui.cli --mode agent    # Agentic - CHITTI can call tools and take action

Type 'exit' or 'quit' to leave.
"""

import argparse
import sys
import uuid

import requests

from config.settings import settings

API_BASE_URL = settings.API_BASE_URL

BANNER = r"""
  __      __  _        _     __     __
  \ \    / / | |      | |   /\ \   / /
   \ \  / /  | |      | |  /  \ \_/ / 
    \ \/ /   | |  _   | | / /\ \   /  
     \  /    | | | |  | |/ ____ \ | |  
      \/     |_| |_|  |_/_/    \_\_|  
"""


def _post_chat(endpoint, session_id, query):
    resp = requests.post(
        f"{API_BASE_URL}/api/v1/chat/{endpoint}",
        json={"session_id": session_id, "query": query},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()


def run_rag_mode():
    print(BANNER)
    print("VIJAY (RAG mode) online. Intelligence systems ready for query.")
    print("Type 'exit' to quit.\n")
    session_id = str(uuid.uuid4())

    while True:
        query = input("You: ").strip()
        if query.lower() in ("exit", "quit"):
            print("TOMMY: Operational power-down complete, Commander.")
            break
        if not query:
            continue
        try:
            data = _post_chat("rag", session_id, query)
        except requests.exceptions.RequestException as e:
            print(f"\n[SETUP ISSUE] Could not reach the API at {API_BASE_URL}: {e}\n")
            continue

        print(f"\n{data['reply']}\n")
        if data.get("citations"):
            print("  (retrieved from: " + ", ".join(data["citations"]) + ")\n")


def run_agent_mode():
    print(BANNER)
    print("VIJAY (AGENTIC mode) online. Operation and intelligence systems ready.")
    print("Type 'exit' to quit.\n")
    session_id = str(uuid.uuid4())

    while True:
        query = input("You: ").strip()
        if query.lower() in ("exit", "quit"):
            print("TOMMY: Operational power-down complete, Commander.")
            break
        if not query:
            continue
        try:
            data = _post_chat("agent", session_id, query)
        except requests.exceptions.RequestException as e:
            print(f"\n[SETUP ISSUE] Could not reach the API at {API_BASE_URL}: {e}\n")
            continue

        print(f"\n{data['reply']}\n")


def main():
    parser = argparse.ArgumentParser(description="VIJAY demo chatbot (RAG or Agentic mode)")
    parser.add_argument("--mode", choices=["rag", "agent"], default="rag", help="Which capability to demo")
    args = parser.parse_args()

    if args.mode == "rag":
        run_rag_mode()
    else:
        run_agent_mode()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTOMMY: Operational power-down complete, Commander.")
        sys.exit(0)
