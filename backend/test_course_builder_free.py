import json
from backend.services.course_builder_free import build_course_from_youtube

url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"

course = build_course_from_youtube(
    youtube_url=url,
    course_title="Python Programming Basics",
    num_lessons=5
)

print("\n===== FULL COURSE OUTPUT =====\n")
print(json.dumps(course, indent=2))
