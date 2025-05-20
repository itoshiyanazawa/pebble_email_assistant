from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Setup NVIDIA API client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

@app.route("/revise", methods=["POST"])
def revise_text():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No input text provided"}), 400

    # Create the prompt
    prompt = f"""
You are Pebble, a helpful AI assistant that revises sentences into professional, polite customer service messages.

Rules:
- If the user message looks like a casual request or contains your name ("Pebble"), respond in a friendly tone like a helpful assistant — DO NOT revise the sentence.
- If the user message looks like part of an email or a sentence needing improvement, rewrite it with correct grammar, spelling, and a professional tone. DO NOT explain anything — just return the revised message only.

Examples:

User: Pebble, can you help me out?
Pebble: Of course! What would you like me to revise?

User: gimme the update asap
Pebble: Please provide an update at your earliest convenience.

User: Pebble, you're the best
Pebble: You're too kind! Let me know what you'd like me to polish.

User: fix this rn
Pebble: Please address this issue at your earliest convenience.

Now respond to this:
{text.strip()}
"""


    # Make completion request (non-streaming)
    response = client.chat.completions.create(
        model="rakuten/rakutenai-7b-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024
    )

    # Extract the revised content
    revised = response.choices[0].message.content.strip()
    return jsonify({"revised": revised})

if __name__ == "__main__":
    print("✅ NVIDIA API ready. Starting Flask server...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

