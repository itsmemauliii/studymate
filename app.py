import gradio as gr
from summarizer import summarize_text
from utils import clean_transcript, chunk_text

def process_transcript(input_text):
    cleaned = clean_transcript(input_text)
    chunks = chunk_text(cleaned)
    summaries = [summarize_text(chunk) for chunk in chunks]
    final_summary = "\n\n".join(summaries)
    return final_summary

app = gr.Interface(
    fn=process_transcript,
    inputs=gr.Textbox(lines=15, placeholder="Paste your YouTube transcript here..."),
    outputs="text",
    title="StudyMate",
    description="Paste a YouTube transcript and get a concise summary to revise smarter!",
)

app.launch()
