import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)

YOUTUBE_REGEX = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"


def extract_video_id(youtube_url: str) -> str | None:
    match = re.search(YOUTUBE_REGEX, youtube_url)
    return match.group(1) if match else None


def get_transcript_from_url(youtube_url: str) -> str | None:
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return None

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join(item["text"] for item in transcript)

    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable):
        return None

    except Exception as e:
        print("Unexpected error:", e)
        return None
