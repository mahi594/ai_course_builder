from services.transcript_service import get_full_transcript
from services.lesson_segmenter_free import segment_transcript_into_lessons

url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"

transcript = get_full_transcript(url)

lessons = segment_transcript_into_lessons(transcript, num_lessons=6)

print("\n===== FREE COURSE STRUCTURE =====\n")
for lesson in lessons["lessons"]:
    print(f"Lesson {lesson['lesson_number']}: {lesson['lesson_title']}")
    print("Key points:", lesson["key_points"])
