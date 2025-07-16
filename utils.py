import re
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def clean_transcript(raw_text):
    cleaned = re.sub(r"\s+", " ", raw_text)
    return cleaned.strip()

def chunk_text(text, max_tokens=400):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

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

