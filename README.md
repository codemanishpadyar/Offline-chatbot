# Offline AI Chatbot (Python + Ollama)

## About the Project

This project is an **offline AI chatbot** created using **Python** and **Ollama**.  
The main goal of this project is to build a chatbot that works **without using any online API or paid service**.

The chatbot runs completely on the local system and uses **local large language models (LLMs)** such as **Phi-3** or **Llama 3** through Ollama.

This project was built for learning purposes and can also be used as a **final year engineering project**.

---

## Features

- Works completely offline
- No API key required
- No internet needed after model download
- Uses local AI models
- Simple command-line chatbot
- Easy to understand and modify

---

## Technologies Used

- Python
- Ollama
- Local LLMs (Phi-3, Llama 3)
- Requests library

---

## Project Files

Offline-AI-Chatbot

├── chatbot_local.py

└── README.md

---

## Step to steup and run
# 1. Download ollama 
https://ollama.com

Check installation: 

bash

ollama --version

---

# 2. Download model 

- Recommended model for low RAM(8GB RAM)systems:

ollama pull phi3

- You can also try:

ollama pull llama3

---

# 3. Install Python Dependency
pip install requests

---

# 4. Run the Chatbot
python chatbot.py
