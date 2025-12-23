import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_notes(topic: str, difficulty: str):
    prompt = f"""
Create concise study notes for:
Topic: {topic}
Level: {difficulty}

Rules:
- 6 to 8 bullet points
- Simple, clear language
- Beginner friendly
"""

    res = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "You are an expert course instructor."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.4
    )


    text = res.choices[0].message.content
    return [line.strip("-• ") for line in text.split("\n") if line.strip()]

def generate_quiz(topic: str, difficulty: str):
    prompt = f"""
    Create 1 multiple-choice quiz question for {topic}
    suitable for a {difficulty} learner.
    """

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        messages=[
            {"role": "system", "content": "You are an expert educator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    text = res.choices[0].message.content.strip()

    return [
        {
            "question": f"What best describes {topic}?",
            "options": [
                "A learning technique",
                "A programming language",
                "A hardware component",
                "A database system"
            ],
            "answer": "A learning technique"
        }
    ]


print("GROQ KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))
