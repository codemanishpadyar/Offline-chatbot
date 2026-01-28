from ai_client import chat_with_ai
from voice_input import listen_voice
from voice_output import speak

def main():
    print(" Offline Voice AI Chatbot (phi3)")
    print("Type 'voice' or 'text' mode\n")

    mode = input("Choose mode: ").lower()

    while True:
        if mode == "voice":
            user_input = listen_voice()
            if not user_input:
                continue
            print("You:", user_input)
        elif mode == "text":
            user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye ")
            speak("Goodbye")
            break

        print(" Thinking...")
        reply = chat_with_ai(user_input)

        print("Chatbot:", reply)
        speak(reply)

if __name__ == "__main__":
    main()
