# 📚 StudyMate

StudyMate is an NLP-powered web app that lets students convert long YouTube transcripts into clean, bullet-style summaries for easier revision.

### Features:
- Accepts YouTube transcript text
- Summarizes using T5 Transformer
- No login or API keys needed
- Free hosting on Hugging Face Spaces

### How to Run:
```bash
pip install -r requirements.txt
python app.py
```
## Future Enhancements

- Auto-fetch transcript using `YouTubeTranscriptAPI`
- Generate quiz questions using `t5` or prompt templates
- Add note export as PDF or Markdown
- Store history for logged-in users
