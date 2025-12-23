import re
import nltk

nltk.download("punkt")

FILLER_PHRASES = [
    "uh", "umm", "you know", "actually", "basically",
    "so guys", "okay guys", "right", "i mean",
    "let me tell you", "kind of", "sort of"
]


def clean_transcript(text: str) -> str:
    """
    Cleans noisy YouTube transcripts:
    - removes filler words
    - removes repeated words
    - fixes spacing
    - removes non-English noise
    """

    if not text:
        return ""

    # Lowercase for normalization
    text = text.lower()

    # Remove filler phrases
    for filler in FILLER_PHRASES:
        text = text.replace(filler, "")

    # Remove non-English / garbage characters
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Sentence tokenize
    sentences = nltk.sent_tokenize(text)

    cleaned_sentences = []
    for s in sentences:
        # Remove very short / useless sentences
        if len(s.split()) < 5:
            continue

        # Capitalize sentence
        cleaned_sentences.append(s.capitalize())

    return " ".join(cleaned_sentences)
