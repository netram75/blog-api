from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    
    # We need to define our columns here!
    # id = ...
    # name = ...
    # role = ...
    # email = ...
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False) 




class Post(Base):
    __tablename__ = "posts"
    
    # We need to define these!
    # id = ...
    # title = ...
    # content = ...
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    
    # This links the post to the specific user who wrote it
    user_id = Column(Integer, ForeignKey("users.id"))

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    
    # Link to the specific user who wrote the comment 🔗
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Link to the specific post the comment is attached to 🔗
    post_id = Column(Integer, ForeignKey("posts.id"))