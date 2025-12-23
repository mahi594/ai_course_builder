import subprocess


def _search(query: str, max_results: int, require_subs: bool):
    """
    Internal helper to search YouTube using yt-dlp
    """

    command = [
        "yt-dlp",
        f"ytsearch{max_results}:{query}",
        "--get-id",
        "--no-warnings"
    ]

    # 🔒 Force captioned videos only
    if require_subs:
        command.extend([
            "--match-filter",
            "subtitles != null"
        ])

    try:
        result = subprocess.check_output(
            command,
            stderr=subprocess.DEVNULL,
            text=True
        )

        video_ids = result.strip().split("\n")

        return [
            f"https://www.youtube.com/watch?v={vid}"
            for vid in video_ids
            if vid
        ]

    except Exception as e:
        print("❌ YouTube search failed:", e)
        return []

def search_youtube_videos(topic, difficulty="beginner", max_results=2):
    query = f"{topic} {difficulty} tutorial"

    command = [
        "yt-dlp",
        f"ytsearch{max_results}:{query}",
        "--get-id",
        "--no-warnings"
    ]

    try:
        result = subprocess.check_output(command, text=True)
        ids = result.strip().split("\n")

        return [
            f"https://www.youtube.com/watch?v={vid}"
            for vid in ids if vid
        ]
    except:
        return []
