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

    return data.get("response", " No response returned")

if __name__ == "__main__":
    print(" Offline AI Chatbot (phi3)")
    print(" Ollama server detected on localhost:11434\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye ")
            break

        print("⏳ Thinking...")
        reply = chat_with_ai(user_input)
        print("Chatbot:", reply)
