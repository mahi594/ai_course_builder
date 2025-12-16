from services.transcript_service import get_full_transcript

url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"
text = get_full_transcript(url)

print("\n===== TRANSCRIPT PREVIEW =====\n")
print(text[:800])
