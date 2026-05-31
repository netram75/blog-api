from pydantic import BaseModel, EmailStr, Field

# user validation blueprint
class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    role: str
    email: EmailStr