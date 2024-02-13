from fastapi.testclient import TestClient

# from .src import app
from src.main import app

client = TestClient(app)


# https://fastapi.tiangolo.com/tutorial/testing/

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_get_item():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": None}


def test_get_user():
    response = client.get("/users/5")
    assert response.status_code == 200
    assert response.json() == {"user_id": 5, "q": None}
