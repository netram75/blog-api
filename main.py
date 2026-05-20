from fastapi import FastAPI, HTTPException

# this is the main application instance
app = FastAPI()

# a simple python dictionary to act as our database for today
fake_user_db = {
    1: {"id":1, "name":"Alice", "role": "Admin"},
    2: {"id":2, "name":"bob", "role":"Author"},
    42: {"id":42, "name":"netram","role": "super user"}
}

# 1. The root endpoint
@app.get('/')
def read_root():
    return {"message":"Welcome to the blogApi"}

# 2. the collection endpoint
@app.get("/users")
def get_all_users():
    return fake_user_db

# 3. the path parameter endpoint
@app.get("/users/{user_id}")
def get_single_user(user_id: int):
    if user_id not in fake_user_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_user_db[user_id]
