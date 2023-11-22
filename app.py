# Backend

import os
import openai
from langchain.llms import OpenAI

# Substitua 'your_api_key' pela API key da OpenAI
os.environ["OPENAI_API_KEY"] = "your_api_key"

llm = OpenAI()

def chatbot_response(prompt):
    system_prompt = (
        "O usuário está perguntando sobre normas de segurança em ambientes industriais. "
        "Responda de forma concisa e clara.\n\n"
    )
    full_prompt = system_prompt + prompt
    response = llm.generate([full_prompt])
    return response

####################################################

# Frontend

import gradio as gr

def chat_interface(prompt):
    response = chatbot_response(prompt)
    return response

interface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Faça sua pergunta aqui..."),
    outputs="text",
    title="Chatbot de Normas de Segurança Industrial",
    description="Pergunte sobre normas de segurança em ambientes industriais."
)

interface.launch()
