from fastapi import APIRouter, HTTPException
# Import our blueprint from the new schemas folder
from schemas.users import User

# create a router instance for user
router = APIRouter()

# In memory user database
fake_user_db = {
    1: {"id": 1, "name": "Alice", "role": "Admin", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "role": "Author", "email": "bob@example.com"},
    42: {"id": 42, "name": "Netram", "role": "Super User", "email": "netram@example.com"}
}

# read all users
@router.get("/users")
def get_users():
    return list(fake_user_db.values())

#read a single user
@router.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id not in fake_user_db:
        raise HTTPException(status_code=404, detail = "user not found")
    return fake_user_db[user_id]

@router.post("/users")
def create_user(new_user: User):
    # 1. Find the highest existing ID and add 1
    new_id = max(fake_user_db.keys()) + 1
    
    # 2. Convert the Pydantic model to a dictionary
    new_user_dict = new_user.model_dump()
    
    # 3. Assign the newly generated ID to the dictionary
    new_user_dict["id"] = new_id
    
    # 4. Save it to our fake database
    fake_user_db[new_id] = new_user_dict
    
    # 5. Return the newly created user
    return new_user_dict

# update a existing user
@router.put("/users/{user_id}")
def update_user(user_id:int, updated_user:User):
    if user_id not in fake_user_db:
        raise HTTPException(status_code=404, detail="user not found")
    fake_user_db[user_id] = updated_user.model_dump()
    return {"message":"user updated successfully", "user":fake_user_db[user_id]}

# delete a user 
@router.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id not in fake_user_db: 
        raise HTTPException(status_code=404, detail="user not found")
    del fake_user_db[user_id]
    return {"message":f"user {user_id} deleted successfully"}

    
