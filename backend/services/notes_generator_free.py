import nltk
from collections import Counter

nltk.download("punkt")


def sentence_score(sentence, keywords):
    score = 0
    words = nltk.word_tokenize(sentence.lower())
    for w in words:
        if w in keywords:
            score += 1
    return score


def generate_notes_for_lesson(transcript, lesson, max_points=5):
    sentences = nltk.sent_tokenize(transcript)

    keywords = set(lesson["key_points"])
    scored = []

    for s in sentences:
        score = sentence_score(s, keywords)
        if score > 0:
            scored.append((score, s))

    # Sort by relevance
    scored.sort(reverse=True, key=lambda x: x[0])

    # Pick top sentences
    selected = [s for _, s in scored[:max_points]]

    notes = {
        "lesson_title": lesson["lesson_title"],
        "notes": selected
    }

    return notes
