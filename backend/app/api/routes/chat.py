from fastapi import APIRouter
from openai import OpenAI
from pydantic import BaseModel
from pymongo import MongoClient

router = APIRouter()

class Prompt(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str
    history: list[str] = []

@router.post("/chat", response_model=ChatResponse)
def chat(prompt: Prompt) -> ChatResponse:
    openai_client = OpenAI()
    mongodb_client = MongoClient("localhost", 27017)

    mongodb_client.chat_db.chat_history.insert_one({"prompt": prompt.prompt});

    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt.prompt
            }
        ]
    )

    documents = mongodb_client.chat_db.chat_history.find()
    history = map(lambda x: x["prompt"], documents)
    return {"response": completion.choices[0].message.content, "history": history}
