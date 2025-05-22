from fastapi import APIRouter, HTTPException
from app.services.video_service import generate_video_prompt

router = APIRouter()

@router.post("/generate-video")
async def generate_video(scene_description: str, additional_context: str = ""):
    try:
        response = generate_video_prompt(scene_description, additional_context)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))