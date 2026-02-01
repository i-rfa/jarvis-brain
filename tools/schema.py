def get_action_schema():
    return [
        {
            "type": "OPEN_APP",
            "description": "Open an app on the phone",
            "args": {
                "package": "Android package name"
            }
        },
        {
            "type": "SPEAK",
            "description": "Speak a message to the user",
            "args": {
                "text": "Text to speak"
            }
        }
    ]
