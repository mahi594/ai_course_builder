import os
from typing import List

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


# -------------------------------------------------
# OpenAI setup (safe)
# -------------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ENABLED = bool(OPENAI_API_KEY and OpenAI)

client = None
if OPENAI_ENABLED:
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception as e:
        print("⚠️ OpenAI init failed:", e)
        OPENAI_ENABLED = False


# -------------------------------------------------
# Notes Rewriter (SMART)
# -------------------------------------------------
def rewrite_notes(notes: List[str]) -> List[str]:
    """
    Converts raw transcript-based notes into clean,
    concise, textbook-style bullet points.
    """

    if not notes:
        return []

    joined_text = "\n".join(notes)

    # ---------- FALLBACK (NO AI) ----------
    if not OPENAI_ENABLED:
        return _simple_cleanup(notes)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert educator.\n"
                        "Convert spoken lecture text into clean, concise study notes.\n"
                        "Rules:\n"
                        "- Remove filler words and repetition\n"
                        "- Rewrite in clear textbook language\n"
                        "- Return 4–6 bullet points\n"
                        "- Do NOT mention the speaker\n"
                    )
                },
                {
                    "role": "user",
                    "content": joined_text
                }
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()
        bullets = [
            line.strip("-• ").strip()
            for line in content.split("\n")
            if line.strip()
        ]

        return bullets

    except Exception as e:
        print("⚠️ rewrite_notes fallback:", e)
        return _simple_cleanup(notes)


# -------------------------------------------------
# Lesson Title Generator (Improved)
# -------------------------------------------------
def generate_lesson_title(keywords: List[str]) -> str:
    if not keywords:
        return "Lesson Overview"

    fallback = " ".join(keywords[:3]).title()

    if not OPENAI_ENABLED:
        return fallback

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Generate a short, professional lesson title "
                        "for an online course."
                    )
                },
                {
                    "role": "user",
                    "content": f"Keywords: {keywords}"
                }
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("⚠️ title fallback:", e)
        return fallback


# -------------------------------------------------
# Simple fallback cleaner (NO AI)
# -------------------------------------------------
def _simple_cleanup(notes: List[str]) -> List[str]:
    cleaned = []
    for n in notes:
        n = n.strip()
        if len(n) < 25:
            continue
        if n.lower().startswith(("i ", "we ", "you ")):
            continue
        cleaned.append(n)
    return cleaned[:5]


def generate_syllabus(topic: str, difficulty: str):
    if not OPENAI_ENABLED:
        return [
            f"introduction to {topic}",
            f"basics of {topic}",
            f"intermediate {topic}",
            f"advanced {topic}",
            f"{topic} projects"
        ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Generate a beginner-friendly course syllabus."},
                {"role": "user", "content": f"Topic: {topic}, Level: {difficulty}"}
            ],
            temperature=0.4
        )
        return response.choices[0].message.content.split("\n")

    except:
        return [
            f"introduction to {topic}",
            f"basics of {topic}",
            f"intermediate {topic}",
            f"advanced {topic}",
            f"{topic} projects"
        ]
