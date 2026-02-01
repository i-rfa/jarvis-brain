import requests
import json
from agent.prompt import SYSTEM_PROMPT
from tools.schema import get_action_schema

OPENAI_API_KEY = "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"

def think(user_text, memory_context):
    actions = get_action_schema()

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Memory context:
{json.dumps(memory_context, indent=2)}

Available actions:
{json.dumps(actions, indent=2)}

User said:
"{user_text}"
"""
            }
        ],
        "temperature": 0.3
    }

    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
