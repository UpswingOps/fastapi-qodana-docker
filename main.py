"""
This is the main file for the FastAPI tutorial
"""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    This is the root path
    :return:
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    This is the item path
    :param item_id:
    :param q:
    :return:
    """
    return {"item_id": item_id, "q": q}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    """
    This is the user path
    :param user_id:
    :param q:
    :return:
    """
    return {"user_id": user_id, "q": q}
