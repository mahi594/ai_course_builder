import requests
import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube_videos(query, difficulty="beginner", max_results=1):
    if not YOUTUBE_API_KEY:
        return []

    search_query = f"{query} {difficulty} tutorial"

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": search_query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    res = requests.get(url, params=params).json()

    videos = []
    for item in res.get("items", []):
        video_id = item["id"]["videoId"]
        videos.append(f"https://www.youtube.com/watch?v={video_id}")

    return videos
