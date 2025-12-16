from backend.services.transcript_cache import get_cached_transcript
from backend.services.lesson_segmenter_free import segment_transcript_into_lessons
from backend.services.notes_generator_free import generate_notes_for_lesson
from backend.services.quiz_generator_free import generate_quiz_for_lesson

url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"

transcript = get_cached_transcript(url)
course = segment_transcript_into_lessons(transcript, num_lessons=5)

print("\n===== COURSE QUIZ =====\n")

for lesson in course["lessons"]:
    notes = generate_notes_for_lesson(transcript, lesson)
    quiz = generate_quiz_for_lesson(lesson, notes)

    print(f"\n📝 {quiz['lesson_title']}")
    for i, q in enumerate(quiz["questions"], 1):
        print(f"\nQ{i}. {q['question']}")
        for opt in q["options"]:
            print(f"  - {opt}")
        print(f"✔ Answer: {q['answer']}")
