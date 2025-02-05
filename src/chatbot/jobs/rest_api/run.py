from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from chatbot.core.chatbot_service import ChatbotService
from chatbot.io.db_connection import get_db, engine
from chatbot.io.db_declaration import Base, ChatMessage


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Creates tables at startup
    yield  # Continue running FastAPI


app = FastAPI(lifespan=lifespan)
chatbot_service = ChatbotService()


# Define input model
class ChatInput(BaseModel):
    message: str

# Define response model
class ChatbotResponse(BaseModel):
    response: str


# Sample chatbot response
@app.post("/chatbot")
async def chatbot(input: ChatInput, db: AsyncSession = Depends(get_db)):
    user_message = input.message.lower()
    
    # Simple chatbot logic
    response = chatbot_service.get_response(user_message)

    # Save message to database
    chat_entry = ChatMessage(user_message=input.message, bot_response=response)
    db.add(chat_entry)
    await db.commit()

    return ChatbotResponse(response=response)

# Run with: uvicorn chatbot.jobs.rest_api.run:app --reload