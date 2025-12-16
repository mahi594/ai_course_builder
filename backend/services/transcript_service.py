from backend.services.youtube import get_transcript_from_url
from backend.services.audio_downloader import download_audio
from backend.services.whisper_service import transcribe_audio


def get_full_transcript(youtube_url: str) -> str:
    # 1️⃣ Try YouTube captions
    text = get_transcript_from_url(youtube_url)
    if text:
        return text

    print("⚠️ Captions unavailable → Using Whisper")

    # 2️⃣ Whisper fallback
    audio_path = download_audio(youtube_url)
    return transcribe_audio(audio_path)
