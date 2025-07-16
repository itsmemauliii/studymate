import streamlit as st
from summarizer import summarize_text
from utils import clean_transcript, chunk_text

st.title("📚 StudyMate")
st.subheader("Paste a YouTube transcript and get a concise summary to revise smarter!")

input_text = st.text_area("Transcript Input", height=300)

if st.button("Summarize"):
    if input_text:
        cleaned = clean_transcript(input_text)
        chunks = chunk_text(cleaned)
        summaries = []
        for chunk in chunks:
            try:
                summary = summarize_text(chunk)
                summaries.append(summary)
            except Exception as e:
                summaries.append(f"[ERROR in chunk]: {e}")
        st.success("✅ Summary Generated!")
        st.write("\n\n".join(summaries))
    else:
        st.warning("Please paste some text first.")
