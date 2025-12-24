import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# ✅ Ensure key exists
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in environment")

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "llama-3.1-8b-instant"  # ✅ WORKING MODEL

def generate_notes(topic: str, difficulty: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": f"Explain {topic} clearly for a {difficulty} learner in bullet points."
            }
        ],
        temperature=0.5,
        max_tokens=400
    )

    text = response.choices[0].message.content
    return [line.strip("- ").strip() for line in text.split("\n") if line.strip()]


def generate_quiz(topic: str, difficulty: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": f"Create 3 quiz questions with answers on {topic} for {difficulty} level."
            }
        ],
        temperature=0.4,
        max_tokens=300
    )

    text = response.choices[0].message.content

    return [
        {
            "question": line,
            "options": [],
            "answer": ""
        }
        for line in text.split("\n") if line.strip()
    ]
