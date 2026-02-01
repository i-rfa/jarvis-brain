import json
import os

MEMORY_FILE = "data/memory.json"

class Memory:
    def __init__(self):
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump({"profile": {}, "history": []}, f)

    def load(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def remember_interaction(self, user, jarvis):
        data = self.load()
        data["history"].append({
            "user": user,
            "jarvis": jarvis
        })
        self.save(data)

    def get_context(self, limit=5):
        data = self.load()
        return data["history"][-limit:]
