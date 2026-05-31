from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

# comments validation blueprint
class Comment(BaseModel):
    id: int
    post_id: int
    test: str = Field(..., min_length=2, max_length=250)
    author_id: int

# in-memory comments database
fake_comment_db = {
    1: {"id": 1, "post_id": 1, "text": "This modular structure makes so much sense!", "author_id": 2},
    2: {"id": 2, "post_id": 1, "text": "Awesome explanation, thanks!", "author_id": 42}
}

# read all comments
@router.get("/comments")
def read_comment():
    return list(fake_comment_db.value())