from fastapi import FastAPI
# import the router we jut created
from routers.users import router as user_router
from routers.posts import router as post_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to the blog api"}

# plug the user router into our main FastAPI application
app.include_router(user_router)

#register the new blog post endpoints
app.include_router(post_router)
