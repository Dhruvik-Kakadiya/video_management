from fastapi import FastAPI
from app.routes import video
from app.database import init_db

app = FastAPI()

# Initialize DB
init_db()

# Register video routes
app.include_router(video.router)


@app.get("/")
def root():
    return {"message": "Video Management API"}
