class ChatbotService:
    def __init__(self):
        pass

    def get_response(self, user_input: str) -> str:
        # Simple logic to generate a response based on user input
        if "hello" in user_input.lower():
            return "Hello! How can I assist you today?"
        elif "bye" in user_input.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I didn't understand that."