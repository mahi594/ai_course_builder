import random
import nltk

nltk.download("punkt")

STOP_WORDS = {
    "this", "that", "here", "there", "will", "want",
    "have", "with", "then", "than", "also", "from",
    "into", "about", "your", "when", "where"
}


def generate_mcq_from_sentence(sentence, keywords):
    words = nltk.word_tokenize(sentence)

    # Valid keyword candidates
    candidates = [
        w for w in words
        if w.lower() in keywords
        and w.lower() not in STOP_WORDS
        and len(w) > 3
    ]

    if not candidates:
        return None

    answer = random.choice(candidates)

    # Create blank safely (single replacement)
    question = sentence.replace(answer, "_____ ", 1)

    # Build distractors
    distractors = list(set(k for k in keywords if k != answer.lower()))
    random.shuffle(distractors)

    if len(distractors) < 3:
        return None

    options = distractors[:3] + [answer]
    random.shuffle(options)

    return {
        "question": question.strip(),
        "options": options,
        "answer": answer
    }


def generate_quiz_for_lesson(lesson, notes, num_questions=3):
    quiz = []
    keywords = set(lesson["key_points"])

    for sentence in notes["notes"]:
        mcq = generate_mcq_from_sentence(sentence, keywords)
        if mcq:
            quiz.append(mcq)

        if len(quiz) == num_questions:
            break

    return {
        "lesson_title": lesson["lesson_title"],
        "questions": quiz
    }
