from typing import Dict
import random
import uuid
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: uuid.UUID
    name: str
    email: str


users: Dict[uuid.UUID, User] = {}


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/users")
def create_user(user: User):
    users[user.id] = user
    return user

@app.post("/users/random")
def create_random_user():
    user = User(id=uuid.uuid4(), name=f"User {random.randint(1, 1000)}", email=f"user{random.randint(1, 1000000)}@example.com")
    users[user.id] = user
    return user


@app.get("/users")
def get_users():
    return users


@app.get("/users/{id}")
def get_user(id: uuid.UUID):
    return users.get(id)
