import yt_dlp
import os

AUDIO_DIR = "data/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


def download_audio(youtube_url: str) -> str:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{AUDIO_DIR}/%(id)s.%(ext)s",
        "quiet": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        return f"{AUDIO_DIR}/{info['id']}.mp3"
