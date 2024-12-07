import random
import gradio as gr

def spec_insight(message, history):
    print(message)
    return "Wireless network"

custom_css = "./custom_chat.css"

app = gr.ChatInterface(
    spec_insight, 
    type="messages", 
    autofocus=False,
    title="SpecInsight: AI Driven Wireless Expert",
    css=custom_css
)
if __name__ == "__main__":
    app.launch()
