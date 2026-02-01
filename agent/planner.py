from agent.memory import Memory

memory = Memory()

def plan(user_text):
    # TEMP: bypass LLM completely
    result = {
        "thought": "Bypass mode – testing core system",
        "actions": [
            {
                "type": "OPEN_APP",
                "args": {
                    "package": "com.whatsapp"
                }
            }
        ],
        "speech": "I am alive. Core system works."
    }

    memory.remember_interaction(user_text, result["speech"])
    return result
