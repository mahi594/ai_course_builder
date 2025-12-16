import sys
import os

# --------------------------------------------------
# Ensure backend/ is in Python path
# --------------------------------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from services.transcript_cache import get_cached_transcript
from services.lesson_segmenter_free import segment_transcript_into_lessons
from services.notes_generator_free import generate_notes_for_lesson


url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"

# Load cached transcript (FAST)
transcript = get_cached_transcript(url)

# Get lessons
course = segment_transcript_into_lessons(transcript, num_lessons=5)

print("\n===== COURSE NOTES =====\n")

for lesson in course["lessons"]:
    notes = generate_notes_for_lesson(transcript, lesson)

    print(f"\n📘 {notes['lesson_title']}")
    for i, point in enumerate(notes["notes"], 1):
        print(f"{i}. {point}")
