#FastAPI
from fastapi import responses
from fastapi.testclient import TestClient

#Main APP
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_create_log():
    body ={

    }
    response = client.post("/log", data=body)
    print(response.json())
    assert response.status_code == 200

