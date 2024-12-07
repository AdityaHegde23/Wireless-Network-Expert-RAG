import random
import gradio as gr

def spec_insight(message, history):
    return "Wireless network"

app = gr.ChatInterface(
    spec_insight, 
    type="messages", 
    autofocus=False,
    title="SpecInsight: AI Driven Wireless Expert"
)
if __name__ == "__main__":
    app.launch()
