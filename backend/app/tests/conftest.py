from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient

from app.main import app

@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module", autouse=True)
def clear_db():
    mongodb_client = MongoClient("localhost", 27017)
    mongodb_client.chat_db.chat_history.delete_many({})

