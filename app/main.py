import time
from config import APP_NAME
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# import the router we jut created
from routers.users import router as user_router
from routers.posts import router as post_router
from routers.comments import router as comment_router

app = FastAPI()

# 2. Define our VIP guest list (origins)
origins = [
    "http://localhost:3000",      # typical React/Next.js port
    "http://127.0.0.1:3000",
    "http://localhost:5173",      # typical Vite/Vue port
]

# 3. Hand the rules to the middleware guard
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Who is allowed?
    allow_credentials=True,       # Allow cookies/authentication?
    allow_methods=["*"],          # Allow all methods (GET, POST, PUT, DELETE)? "*" means yes!
    allow_headers=["*"],          # Allow all headers?
)

# ⏱️ Custom Timing Middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()                   # 1. Start the stopwatch
    response = await call_next(request)        # 2. Pass the request to the routers
    process_time = time.time() - start_time    # 3. Stop the stopwatch
    response.headers["X-Process-Time"] = str(process_time) # 4. Stamp the time on the response
    return response

@app.get("/")
def read_root():
    return {"message": f"welcome to {APP_NAME}!"}

# plug the user router into our main FastAPI application
app.include_router(user_router)

#register the new blog post endpoints
app.include_router(post_router)

app.include_router(comment_router)
