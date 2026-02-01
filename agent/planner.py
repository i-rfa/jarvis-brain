import json
from agent.llm import think
from agent.memory import Memory

memory = Memory()

def extract_json(text):
    if not text:
        return None

    start = text.find("{")
    end = text.rfind("}") + 1

    if start == -1 or end == -1:
        return None

    try:
        return json.loads(text[start:end])
    except Exception:
        return None

def plan(user_text):
    context = memory.get_context()

    raw = think(user_text, context)
    result = extract_json(raw)

    if not result:
        result = {
            "thought": "LLM failed to respond correctly",
            "actions": [],
            "speech": "I had trouble thinking. Please try again."
        }

    memory.remember_interaction(user_text, result.get("speech", ""))
    return result
