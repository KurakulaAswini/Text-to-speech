# -*- coding: utf-8 -*-
"""Copy of run.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZQeXFdoBCEk9s4x5rOhTlG62pHyXt0TS

# Gradio Demo: automatic-speech-recognition
### Automatic speech recognition English. Record from your microphone and the app will transcribe the audio.
"""

!pip install -q gradio

import gradio as gr
import os

# save your HF API token from https:/hf.co/settings/tokens as an env variable to avoid rate limiting
auth_token = os.getenv("auth_token")

# automatically load the interface from a HF model
# you can remove the api_key parameter if you don't care about rate limiting.
demo = gr.load(
    "huggingface/facebook/wav2vec2-base-960h",
    title="Text-to-speech",
    inputs="mic",
    description="Let me try to guess what you're saying!",
    hf_token=auth_token
)

demo.launch()