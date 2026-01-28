import requests

URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

def chat_with_ai(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(URL, json=payload, timeout=300)
    data = response.json()

    return data.get("response", "No response returned")
