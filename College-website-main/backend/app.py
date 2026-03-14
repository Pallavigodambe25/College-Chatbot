from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
from rag_engine import search
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ------------------------------
# Serve the frontend website
# ------------------------------
@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")


# ------------------------------
# Chatbot API
# ------------------------------
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    context = search(user_message)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant for the PVPIT college website. Answer using the following notices:\n" + context
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        model="llama-3.1-8b-instant"
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})


# ------------------------------
# Run Flask server
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)