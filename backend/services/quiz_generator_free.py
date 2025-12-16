import random
import nltk

nltk.download("punkt")

STOP_WORDS = {
    "this", "that", "here", "there", "will", "want",
    "have", "with", "then", "than", "also"
}


def generate_mcq_from_sentence(sentence, keywords):
    words = nltk.word_tokenize(sentence)

    # Pick valid answer candidates
    candidates = [
        w for w in words
        if w.lower() in keywords and w.lower() not in STOP_WORDS
    ]

    if not candidates:
        return None

    answer = random.choice(candidates)

    question_text = sentence.replace(answer, "_____").strip().capitalize()

    # Build options
    distractors = [
        k for k in keywords
        if k.lower() != answer.lower()
    ]

    if len(distractors) < 3:
        return None

    random.shuffle(distractors)
    options = distractors[:3] + [answer]
    random.shuffle(options)

    return {
        "question": question_text,
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

        if len(quiz) >= num_questions:
            break

    return {
        "lesson_title": lesson["lesson_title"],
        "questions": quiz
    }
