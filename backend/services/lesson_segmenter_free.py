def normalize_transcript(text):
    if isinstance(text, list):
        return " ".join(
            t["text"] if isinstance(t, dict) and "text" in t else str(t)
            for t in text
        )
    return str(text)


def segment_transcript_into_lessons(transcript, num_lessons=5):

    transcript = normalize_transcript(transcript)

    if not transcript.strip():
        raise Exception("Empty transcript")

    words = transcript.split()
    total_words = len(words)

    chunk_size = max(1, total_words // num_lessons)

    lessons = []

    for i in range(num_lessons):
        start = i * chunk_size
        end = start + chunk_size

        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        lessons.append({
            "lesson_number": i + 1,
            "content": chunk_text,
            "key_points": chunk_words[:5]
        })

    return {"lessons": lessons}
