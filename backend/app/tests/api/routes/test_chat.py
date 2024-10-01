from app.core.config import settings
from app.api.routes.chat import chat
from fastapi.testclient import TestClient


def test_when_called_with_incorrect_body_format_returns_error(
    client: TestClient
) -> None:
    r = client.post(f"{settings.API_V1_STR}/chat", json={"this": "is wrong"})
    content = r.json()
    assert content
    assert r.status_code == 422

def test_when_called_forwards_to_llm(
        client: TestClient
) -> None:
    r = client.post(f"{settings.API_V1_STR}/chat", json={"prompt": "Hello"})
    content = r.json()
    assert content['response']
    assert r.status_code == 200
