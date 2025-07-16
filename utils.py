import re
import nltk
from nltk.tokenize import sent_tokenize

# Make sure 'punkt' tokenizer is downloaded for sentence splitting
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

def clean_transcript(raw_text):
    """
    Removes extra whitespace from transcript text.
    """
    cleaned = re.sub(r"\s+", " ", raw_text)
    return cleaned.strip()

def chunk_text(text, max_tokens=400):
    """
    Splits the cleaned transcript into smaller chunks of sentences,
    each having fewer than `max_tokens` words (for safe model input).
    """
    sentences = sent_tokenize(text)
    chunks, chunk = [], ""

    for sent in sentences:
        if len(chunk.split()) + len(sent.split()) < max_tokens:
            chunk += " " + sent
        else:
            chunks.append(chunk.strip())
            chunk = sent

    if chunk:
        chunks.append(chunk.strip())

    return chunks
