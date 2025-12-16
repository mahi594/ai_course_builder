from backend.services.transcript_cache import get_cached_transcript
from backend.services.lesson_segmenter_free import segment_transcript_into_lessons
from backend.services.notes_generator_free import generate_notes_for_lesson
from backend.services.quiz_generator_free import generate_quiz_for_lesson


def build_course_from_youtube(
    youtube_url: str,
    course_title: str = "Auto Generated Course",
    num_lessons: int = 5
) -> dict:
    """
    Builds a full course (lessons + notes + quizzes)
    from a YouTube video.
    """

    # 1️⃣ Get transcript (cached)
    transcript = get_cached_transcript(youtube_url)

    # 2️⃣ Segment lessons
    lesson_data = segment_transcript_into_lessons(
        transcript,
        num_lessons=num_lessons
    )

    full_course = {
        "course_title": course_title,
        "source": youtube_url,
        "lessons": []
    }

    # 3️⃣ Generate notes + quiz for each lesson
    for lesson in lesson_data["lessons"]:
        notes = generate_notes_for_lesson(transcript, lesson)
        quiz = generate_quiz_for_lesson(lesson, notes)

        full_course["lessons"].append({
            "lesson_number": lesson["lesson_number"],
            "lesson_title": lesson["lesson_title"],
            "key_points": lesson["key_points"],
            "notes": notes["notes"],
            "quiz": quiz["questions"]
        })

    return full_course
