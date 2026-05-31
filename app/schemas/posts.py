from pydantic import BaseModel, Field


# post validation blueprint
class Post(BaseModel):
    id: int 
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=10)
    author_id: int