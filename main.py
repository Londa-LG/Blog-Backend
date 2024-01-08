from models import Base
from database import engine
from fastapi import FastAPI
from routers import posts, users, comments, authentication

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(comments.router)
app.include_router(authentication.router)
