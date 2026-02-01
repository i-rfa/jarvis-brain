import json
import openai
from agent.prompt import SYSTEM_PROMPT
from tools.schema import get_action_schema

openai.api_key = "PASTE_YOUR_API_KEY"

def think(user_text, memory_context):
    actions = get_action_schema()

    prompt = f"""
Memory context:
{json.dumps(memory_context, indent=2)}

Available actions:
{json.dumps(actions, indent=2)}

User said:
"{user_text}"
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return json.loads(response.choices[0].message.content)
