# src/brain/api.py

import requests

# Backend LLM server URL
URL = "https://llm.overlord-loki.com"


def get_response(backend_conversation_history) -> str:
    data = {"messages": backend_conversation_history}
    response = requests.post(f"{URL}/chat", json=data)

    # Ensure the response is not empty and strip any extra whitespace
    response_text = response.json().get("response", "").strip()

    return response_text
