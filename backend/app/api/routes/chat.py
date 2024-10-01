from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/chat", response_model=str)
def chat() -> Any:
    return "Working!"
