from agent.llm import think
from agent.memory import Memory

memory = Memory()

def plan(user_text):
    context = memory.get_context()
    result = think(user_text, context)
    memory.remember_interaction(user_text, result.get("speech", ""))
    return result
