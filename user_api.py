from fastapi import FastAPI
import os

app = FastAPI()

# Dummy data for demonstration
users = {
    1: {"name": "John", "age": 30},
    2: {"name": "Jane", "age": 25},
}

# Fetch build version from the environment variable
def get_build_version():
    build_version = os.getenv("BUILD_VERSION", "Unknown")
    return build_version

@app.get("/version")
async def version():
    return {"version": get_build_version()}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    return {"message": "User not found"}

@app.get("/users/2/{user_id}")
async def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    return {"message": "User not found"}


""" uvicorn user_api:app --reload """