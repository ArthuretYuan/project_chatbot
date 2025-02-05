import requests

API_URL = "http://127.0.0.1:8000/chatbot"

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = requests.post(API_URL, json={"message": user_input})
        bot_reply = response.json()["response"]
        print(f"Chatbot: {bot_reply}")

# Run the chatbot
chat()