from fastapi import APIRouter
from openai import OpenAI
from pydantic import BaseModel

router = APIRouter()

class Prompt(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
def chat(prompt: Prompt) -> ChatResponse:
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt.prompt
            }
        ]
    )
    return {"response": completion.choices[0].message.content}
