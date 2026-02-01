from flask import Flask, request, jsonify
from agent.agent import JarvisAgent

app = Flask(__name__)
jarvis = JarvisAgent()

@app.route("/think", methods=["POST"])
def think():
    data = request.json
    user_text = data.get("text", "")

    result = jarvis.process(user_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
