# Offline Voice-Enabled AI Chatbot (Ollama + Phi-3)

This project is a simple **offline AI chatbot** built using **Python** and **Ollama (phi-3 model)**.  
It supports both **text input** and **voice commands**, and can also **speak back** the responses using text-to-speech.

---

## Features

- Fully **offline AI chatbot** using Ollama
- Supports **text mode** and **voice mode**
- **Speech-to-Text** for voice commands
- **Text-to-Speech** for spoken responses

---

##  Technologies Used

- Python  
- Ollama (phi-3 model)  
- `requests` – API communication  
- `speechrecognition` – voice input  
- `pyttsx3` – text to speech  
- `pyaudio` – microphone access  

---
## Project Structure

```bash
Offline-chatbot/
│
├── main.py 
├── ai_client.py  
├── voice_input.py 
├── voice_output.py  
└── README.md
```

---

##  Setup Instructions

### _1._ Install Ollama
#### Download and install Ollama from:

https://ollama.com

Pull the Phi-3 model:
```bash
ollama pull phi3
```

## Start ollama
```bash
ollama run phi3
```

### _2._ Install Python Dependencies

```bash
pip install pipwin
pipwin install pyaudio
```

---

*“From silence to speech — the beginning of my AI voice chatbot journey.”*