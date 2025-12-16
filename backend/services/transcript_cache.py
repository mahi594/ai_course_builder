import os
from backend.services.transcript_service import get_full_transcript


# Folder to store cached transcripts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE_DIR, "data", "transcripts")

os.makedirs(CACHE_DIR, exist_ok=True)


def get_cached_transcript(youtube_url: str) -> str:
    video_id = youtube_url.split("v=")[-1]
    cache_path = os.path.join(CACHE_DIR, f"{video_id}.txt")

    # Load from cache if exists
    if os.path.exists(cache_path):
        print("📂 Loading transcript from cache")
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    # Otherwise generate transcript once
    print("🎙️ Generating transcript (first time only)")
    transcript = get_full_transcript(youtube_url)

    with open(cache_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript
