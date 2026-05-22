from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()

# post validation blueprint
class Post(BaseModel):
    id: int 
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=10)
    author_id: int

# in memory blog post database
fake_post_db = {
    1: {"id":1, "title":"Getting Started with FastAPI", "content":"FastAPI is a modern, fast web framework for building APIs with Python.", "authod_id":42},
    2:{"id":2, "title":"Understanding Routers", "content":"Routers help keep your backend code clean, organized, and modular.", "author_id":1}
}

# read all posts
@router.get("/posts")
def get_posts():
    return list(fake_post_db.values())

# read a single post
@router.get("/posts/{post_id}")
def get_post(post_id:int):
    if post_id not in fake_post_db:
        raise HTTPException(status_code=404, detail="post not found")
    return fake_post_db[post_id]

# create a brand new post (use 201 created!)
@router.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    if new_post.id in fake_post_db:
        raise HTTPException(status_code=400, detail="post with this id already exist")
    
    fake_post_db[new_post.id] = new_post.model_dump()
    return fake_post_db[new_post.id]

#update an existing post
@router.put("/posts/{post_id}")
def update_post(post_id:int, updated_post:Post):
    if post_id not in fake_post_db:
        raise HTTPException(status_code=404, detail="post not found")
    
    fake_post_db[post_id] = updated_post.model_dump()
    return {"message": "post updated successfully", "post":fake_post_db[post_id]}

# delete a post(uses 204 not content!)
@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id:int):
    if post_id not in fake_post_db:
        raise HTTPException(status_code=404, detail="post not found")
    
    del fake_post_db[post_id]
    # with a 204 status With a 204 status code, FastAPI automatically ignores any return statement body because a 204 response is strictly forbidden from carrying data payload.
    return None
    

