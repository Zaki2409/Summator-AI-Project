# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from app.services.video_service import generate_video_prompt, generate_actual_video
# from typing import Optional

# router = APIRouter()

# # Request model
# class VideoRequest(BaseModel):
#     scene_description: str
#     additional_context: Optional[str] = None

# # Response model
# class VideoResponse(BaseModel):
#     status: str
#     video_url: Optional[str] = None
#     prompts: Optional[dict] = None
#     error: Optional[str] = None

# @router.post("/generate-video", response_model=VideoResponse)
# async def generate_video(request: VideoRequest):
#     """
#     Generate video from scene description with the following flow:
#     1. First generate detailed scene prompts
#     2. Then convert the best prompt into actual video
#     3. Return both the prompts and video URL
#     """
#     try:
#         # Step 1: Generate scene prompts
#         prompts = generate_video_prompt(
#             request.scene_description,
#             request.additional_context or ""
#         )
        
#         # Step 2: Generate actual video from the first prompt variation
#         if prompts and "promptVariations" in prompts and len(prompts["promptVariations"]) > 0:
#             video_url = generate_actual_video(
#                 prompts["promptVariations"][0]["prompt"]
#             )
#         else:
#             raise ValueError("No valid prompts generated")
        
#         return {
#             "status": "success",
#             "video_url": video_url,
#             "prompts": prompts
#         }
        
#     except Exception as e:
#         return {
#             "status": "error",
#             "error": str(e),
#             "video_url": None,
#             "prompts": None
#         }


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