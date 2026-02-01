import requests
import json
from agent.prompt import SYSTEM_PROMPT
from tools.schema import get_action_schema

OPENAI_API_KEY = "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"

OPENAI_URL = "https://api.openai.com/v1/chat/completions"

def think(user_text, memory_context):
    actions = get_action_schema()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
Memory:
{json.dumps(memory_context, indent=2)}

Allowed actions:
{json.dumps(actions, indent=2)}

User said:
\"{user_text}\"

Respond ONLY with valid JSON.
"""
        }
    ]

    payload = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.2
    }

    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        OPENAI_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        return ""

    return response.text
