import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter

nltk.download("punkt")


def split_into_chunks(text, max_sentences=6):
    sentences = nltk.sent_tokenize(text)
    chunks = []

    for i in range(0, len(sentences), max_sentences):
        chunks.append(" ".join(sentences[i:i + max_sentences]))

    return chunks


CUSTOM_STOPWORDS = {
    "this", "that", "here", "there", "with", "have", "going",
    "would", "could", "should", "also", "like", "just",
    "about", "your", "than", "then", "very", "much",
    "into", "from", "using", "use", "used"
}


def extract_keywords(text, top_n=5):
    words = [
        w.lower()
        for w in nltk.word_tokenize(text)
        if w.isalpha()
        and len(w) > 3
        and w.lower() not in CUSTOM_STOPWORDS
    ]
    return [w for w, _ in Counter(words).most_common(top_n)]


def segment_transcript_into_lessons(transcript, num_lessons=6):
    chunks = split_into_chunks(transcript)

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=3000
    )

    X = vectorizer.fit_transform(chunks)

    kmeans = KMeans(
        n_clusters=num_lessons,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X)

    lessons = {}
    for idx, label in enumerate(labels):
        lessons.setdefault(label, []).append(chunks[idx])

    result = []
    for texts in lessons.values():
        combined = " ".join(texts)
        keywords = extract_keywords(combined)

        result.append({
            "lesson_number": len(result) + 1,
            "lesson_title": " ".join(keywords[:2]).title() + " Concepts",
            "key_points": keywords
        })

    return {"lessons": result}
