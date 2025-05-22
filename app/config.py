import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VIDEO_API_KEY = os.getenv("VIDEO_API_KEY")
    SUMMARY_API_KEY = os.getenv("SUMMARY_API_KEY")
    VIDEO_API_HOST = "openai-sora-ai-video-prompt-generator-cinematic-api.p.rapidapi.com"
    SUMMARY_API_HOST = "article-extractor-and-summarizer.p.rapidapi.com"