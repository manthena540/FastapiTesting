from fastapi import FastAPI

app = FastAPI()

# Dummy data for demonstration
users = {
    1: {"name": "John", "age": 30},
    2: {"name": "Jane", "age": 25},
}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    return {"message": "User not found"}

@app.get("/users2/{user_id}")
async def read_user(user_id: int):
    if user_id in users:
        return users[user_id]
    return {"message": "User not found"}

""" uvicorn user_api:app --reload """