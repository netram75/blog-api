from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

# this is the main application instance
app = FastAPI()

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    role: str
    email: EmailStr


# a simple python dictionary to act as our database for today
fake_user_db = {
    1: {"id": 1, "name": "Alice", "role": "Admin", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "role": "Author", "email": "bob@example.com"},
    42: {"id": 42, "name": "Netram", "role": "Super User", "email": "netram@example.com"}
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

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id not in fake_user_db:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    #save the updated data back into our fake database
    fake_user_db[user_id] = updated_user.model_dump()
    return {"message":"User updated Successfully", "user": updated_user}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # remove the user from our fake database
    del fake_user_db[user_id]
    return {"message": f"user {user_id} deleted successfully"}
