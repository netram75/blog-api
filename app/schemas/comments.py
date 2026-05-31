from pydantic import BaseModel, Field

# comments validation blueprint
class Comment(BaseModel):
    id: int
    post_id: int
    test: str = Field(..., min_length=2, max_length=250)
    author_id: int