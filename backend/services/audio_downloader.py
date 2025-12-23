import os
import subprocess
import uuid

AUDIO_DIR = "data/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


def download_audio(youtube_url: str) -> str:
    audio_id = str(uuid.uuid4())
    output_path = os.path.join(AUDIO_DIR, audio_id)

    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--no-playlist",
        "--extract-audio",
        "--audio-format", "wav",
        "-o", f"{output_path}.%(ext)s",
        youtube_url
    ]

    subprocess.run(command, check=True)

    return f"{output_path}.wav"
