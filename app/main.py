from fastapi import FastAPI
from app.api.video import router as video_router
from app.api.summary import router as summary_router

app = FastAPI()

app.include_router(video_router, prefix="/api/v1")
app.include_router(summary_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Text Summarizer and Video Generator API"}