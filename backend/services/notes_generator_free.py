import nltk

# ❌ REMOVE nltk.download("punkt") from here


def sentence_score(sentence, keywords):
    words = nltk.word_tokenize(sentence.lower())
    return sum(1 for w in words if w in keywords)


def generate_notes_for_lesson(transcript, lesson, max_points=5):
    sentences = nltk.sent_tokenize(transcript)
    keywords = set(k.lower() for k in lesson["key_points"])

    scored = []

    for s in sentences:
        s = s.strip()

        # Skip very short or very long sentences
        if len(s) < 20 or len(s) > 200:
            continue

        score = sentence_score(s, keywords)
        if score > 0:
            scored.append((score, s))

    # Sort by relevance
    scored.sort(key=lambda x: x[0], reverse=True)

    # Remove duplicates & pick top
    selected = []
    seen = set()

    for _, s in scored:
        if s not in seen:
            selected.append(s)
            seen.add(s)
        if len(selected) >= max_points:
            break

    # Fallback if nothing matched
    if not selected:
        selected = sentences[:max_points]

    return {
        "lesson_title": lesson["lesson_title"],
        "notes": selected
    }
