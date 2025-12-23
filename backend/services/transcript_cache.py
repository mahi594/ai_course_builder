import os, json, hashlib
from backend.services.transcript_service import get_full_transcript

CACHE_DIR = "data/transcripts"
os.makedirs(CACHE_DIR, exist_ok=True)
MAX_CHARS = 6000


def _cache_path(url: str) -> str:
    key = hashlib.md5(url.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{key}.json")


def get_cached_transcript(youtube_url: str) -> str:
    path = _cache_path(youtube_url)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            transcript = data.get("transcript", "")
            if isinstance(transcript, list):
                transcript = " ".join(transcript)
            return transcript

    transcript = get_full_transcript(youtube_url)

    if len(transcript) > MAX_CHARS:
        transcript = transcript[:MAX_CHARS]

    with open(path, "w", encoding="utf-8") as f:
        json.dump({"transcript": transcript}, f)

    return transcript
