from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.core.chatbot_service import ChatbotService

app = FastAPI()
chatbot_service = ChatbotService()


# Define input model
class ChatInput(BaseModel):
    message: str

# Sample chatbot response
@app.post("/chatbot")
async def chatbot(input: ChatInput):
    user_message = input.message.lower()
    
    # Simple chatbot logic
    response = chatbot_service.get_response(user_message)

    return {"response": response}

# Run with: uvicorn chatbot.jobs.rest_api.run:app --reload