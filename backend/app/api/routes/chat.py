import itertools

from fastapi import APIRouter
from openai import OpenAI
from pydantic import BaseModel
from pymongo import MongoClient

router = APIRouter()

class Prompt(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str
    prompts: list[str] = []

@router.post("/chat", response_model=ChatResponse)
def chat(prompt: Prompt) -> ChatResponse:
    openai_client = OpenAI()
    mongodb_client = MongoClient("localhost", 27017)

    documents = mongodb_client.chat_db.chat_history.find()

    prompts = map(lambda x: {"role": "user", "content": x["prompt"]}, documents)
    responses = map(lambda x: {"role": "assistant", "content": x["response"]}, documents)
    history = list(itertools.chain(*list(zip(prompts, responses))))

    messages = history + [{"role": "user", "content": prompt.prompt}]

    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = completion.choices[0].message.content

    mongodb_client.chat_db.chat_history.insert_one({"prompt": prompt.prompt, "response": response});

    documents = mongodb_client.chat_db.chat_history.find()
    prompt_history = map(lambda x: x["prompt"], documents)

    return {"response": response, "prompts": prompt_history}
