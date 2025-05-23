from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.video_service import generate_video_prompt, generate_actual_video
from fastapi.responses import FileResponse
import os

router = APIRouter()

class VideoRequest(BaseModel):
    scene_description: str
    additional_context: str = ""

@router.post("/generate-video")
async def create_video(request: VideoRequest):
    try:
        # Step 1: Generate prompts
        prompts = generate_video_prompt(
            request.scene_description,
            request.additional_context
        )
        
        # Step 2: Generate video - pass the ENTIRE prompts dict
        video_result = generate_actual_video(prompts)  # Not prompts["promptVariations"][0]["prompt"]
        
        if video_result["status"] == "error":
            raise HTTPException(status_code=400, detail=video_result["message"])
        
        # Return the video file
        return FileResponse(
            video_result["video_path"],
            media_type="video/mp4",
            filename="generated_video.mp4"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))