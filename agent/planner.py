import json
from agent.llm import think
from agent.memory import Memory

memory = Memory()

def plan(user_text):
    context = memory.get_context()

    raw = think(user_text, context)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        result = {
            "thought": "Failed to parse LLM output",
            "actions": [],
            "speech": "I had trouble understanding that. Can you rephrase?"
        }

    memory.remember_interaction(user_text, result.get("speech", ""))
    return result
