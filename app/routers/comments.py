from fastapi import APIRouter
# Import our blueprint from the new schemas folder
from schemas.comments import Comment

router = APIRouter()


# in-memory comments database
fake_comment_db = {
    1: {"id": 1, "post_id": 1, "text": "This modular structure makes so much sense!", "author_id": 2},
    2: {"id": 2, "post_id": 1, "text": "Awesome explanation, thanks!", "author_id": 42}
}

# read all comments
@router.get("/comments")
def read_comment():
    return list(fake_comment_db.value())