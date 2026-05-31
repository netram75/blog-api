from fastapi import APIRouter, HTTPException, status
# Import our blueprint from the new schemas folder
from schemas.posts import Post
router = APIRouter()



# in memory blog post database
fake_post_db = {
    1: {"id":1, "title":"Getting Started with FastAPI", "content":"FastAPI is a modern, fast web framework for building APIs with Python.", "authod_id":42},
    2:{"id":2, "title":"Understanding Routers", "content":"Routers help keep your backend code clean, organized, and modular.", "author_id":1}
}

# read all posts
@router.get("/posts")
def get_posts(author_id: int | None = None, search: str | None = None, offset: int = 0, limit: int = 10):
    # start with all post from our fake database
    results = list(fake_post_db.values())

    #check: Did the user passes an author_id query parameter
    if author_id is not None:
        #keep only the post where the author_id matches
        results = [post for post in results if post["author_id"] == author_id]

    # search by text if provided
    if search is not None:
        # Check if the search term is in the title OR the content (case-insensitive)
        results = [
            post for post in results 
            if search.lower() in post["title"].lower() or search.lower() in post["content"].lower()
        ]

    #apply the limit slicing (e.g. , [:10] returns the first 10 items)
    return results[offset : offset + limit]

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
    

