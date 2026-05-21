import gradio as gr
from app.services.summarizer import cached_summarize


# Call summarize.py from app.services
def summarize_text(text, language, length):

    # Handle empty input
    if not text.strip():
        return "Please enter some text.", ""
    
    try:
        # Limit input size
        text = text[:2000]

        # Use cached version (having lazy run) to generate the summary
        summary = cached_summarize(text, language, length)

        # Stats
        words = len(summary.split())
        reading_time = round(words / 3)

        stats = f"Words: {words} | ⏱️ {reading_time} sec"

        return summary, stats

    except Exception as e:
        return f"❌ Error: {str(e)}", ""


# Character counter
def count_chars(text):
    return f"Characters: {len(text)}"

# Clear function
def clear_all():
    return "", "Characters: 0", "", "Words: 0 | Reading time: 0 sec"

# File generator
def create_file(text):
    if not text:
        return None
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return "summary.txt"


# UI using Blocks
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    # Header
    gr.Markdown("Multi language NLP Tool")
    gr.Markdown("Summarize & Translate Multi language  using AI")

    # Input Instructions
    gr.Markdown("👉 Paste text → choose options → click Summarize")

    # Input Section
    gr.Markdown("## Input")
    gr.Markdown("Paste text using Ctrl+V/ Cmd+V")
    
    # Input
    text_input = gr.Textbox(
        lines=10,
        placeholder="Enter text here...",
        label="Input Text"
    )
    char_count = gr.Markdown("Characters: 0")

    # Controls
    gr.Markdown("## Options")

    with gr.Row():
        language = gr.Dropdown(["bn", "en", "hi"],value="bn",label="Language")
        length = gr.Radio(["short", "medium", "long"],value="medium",label="Summary Length")

    # Buttons
    with gr.Row():
        submit_btn = gr.Button("Summarize", variant="primary")
        clear_btn = gr.Button("Clear")
    
    # Output Section
    gr.Markdown("## 📄 Summary")
    summary_output = gr.Textbox(label="Summary")
    stats_output = gr.Markdown("Words: 0 | Reading time: 0 sec")

    gr.Markdown("⚠️ AI-generated summaries may not be 100% accurate.")

    # Download
    download_file = gr.File(label="Download Summary")

    # Copy
    gr.Markdown("💡 Tip: Click inside summary box and press Ctrl+C to copy")
 
    # Interactions
    text_input.change(fn=count_chars, inputs=text_input, outputs=char_count)

    submit_btn.click(
        fn = lambda: ("⏳ Processing...Please wait..",""),
        outputs=[summary_output, stats_output]
    ).then(
        fn=summarize_text,
        inputs=[text_input, language, length],
        outputs=[summary_output, stats_output]
    )

    clear_btn.click(
        fn=clear_all,
        outputs=[text_input, char_count, summary_output, stats_output]
    )

    summary_output.change(
        fn=create_file,
        inputs=summary_output,
        outputs=download_file
    )

    # Footer
    gr.Markdown("---")
    gr.Markdown("⚡ Built with FastAPI + Transformers + Gradio ")

# Run app
if __name__ == "__main__":
    demo.queue()
    demo.launch(server_name="0.0.0.0", server_port=7860) 