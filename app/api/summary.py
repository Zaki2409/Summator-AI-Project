from fastapi import APIRouter, HTTPException
from app.services.summary_service import summarize_article

router = APIRouter()

@router.get("/summarize")
async def summarize(url: str):
    try:
        response = summarize_article(url)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))