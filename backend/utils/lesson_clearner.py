import re

FILLER_PATTERNS = [
    r"\bin this video\b",
    r"\bi will tell you\b",
    r"\bwe will talk about\b",
    r"\byou guys\b",
    r"\bso friends\b",
    r"\bokay\b",
    r"\bactually\b",
    r"\bbasically\b"
]

def clean_sentence(sentence: str) -> str:
    text = sentence.lower()

    # Remove filler phrases
    for pattern in FILLER_PATTERNS:
        text = re.sub(pattern, "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Capitalize
    return text.capitalize()


def clean_notes(notes: list[str]) -> list[str]:
    cleaned = []
    seen = set()

    for note in notes:
        s = clean_sentence(note)

        # Remove very short or duplicate lines
        if len(s) < 25:
            continue
        if s in seen:
            continue

        seen.add(s)
        cleaned.append(s)

    return cleaned
