import json
from backend.services.course_builder_free import build_course_from_topic

topic = "Python for Data Science"
difficulty = "beginner"

course = build_course_from_topic(
    topic=topic,
    difficulty=difficulty,
    videos_per_topic=1
)

print("\n===== AI GENERATED COURSE FROM TOPIC =====\n")
print(json.dumps(course, indent=2))
