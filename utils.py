import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def clean_transcript(raw_text):
    cleaned = re.sub(r"\s+", " ", raw_text)
    return cleaned.strip()

def chunk_text(text, max_tokens=400):
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
