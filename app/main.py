from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.video import router as video_router
from app.api.summary import router as summary_router

app = FastAPI()

# Serve generated videos
app.mount("/videos", StaticFiles(directory="video_outputs"), name="videos")

app.include_router(video_router, prefix="/api/v1")
#app.include_router(video_router, prefix="/api/v1")
app.include_router(summary_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Text Summarizer and Video Generator API"}