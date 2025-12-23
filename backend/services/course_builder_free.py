from backend.services.youtube_search import search_youtube_videos
from backend.services.syllabus_generator import get_course_syllabus
from backend.services.recommendation_service import recommend_courses
from backend.services.ai_content_generator import generate_notes, generate_quiz

def build_course_from_topic(topic: str, difficulty="beginner"):
    syllabus = get_course_syllabus(topic, difficulty)

    course = {
        "course_title": f"{topic.title()} ({difficulty.title()})",
        "difficulty": difficulty,
        "modules": [],
        "recommendations": recommend_courses(topic)
    }

    for i, unit in enumerate(syllabus, 1):
        videos = search_youtube_videos(unit, difficulty, max_results=1)
        video_url = videos[0] if videos else None

        # ✅ AI-generated notes (ALWAYS list[str])
        notes = generate_notes(unit, difficulty)

        # ✅ AI-generated quiz (ALWAYS list[dict])
        quiz = generate_quiz(unit, difficulty)
        

        module = {
            "module_title": f"Module {i}: {unit}",
            "video_url": video_url,
            "notes": notes,   # ✅ FIXED
            "quiz": quiz
        }

        course["modules"].append(module)

    return course
