import http.client
import json
from app.config import Config

def make_video_api_request(payload_data):
    conn = http.client.HTTPSConnection(Config.VIDEO_API_HOST)
    payload = json.dumps(payload_data)
    headers = {
        'x-rapidapi-key': Config.VIDEO_API_KEY,
        'x-rapidapi-host': Config.VIDEO_API_HOST,
        'Content-Type': "application/json"
    }
    conn.request("POST", "/generateScenePrompts?mood=dramatic&style=cinematic&language=en&noqueue=1", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))  # ✅ Parsed JSON

def make_summary_api_request(url):
    conn = http.client.HTTPSConnection(Config.SUMMARY_API_HOST)
    
    headers = {
        'x-rapidapi-key': Config.SUMMARY_API_KEY,
        'x-rapidapi-host': Config.SUMMARY_API_HOST
    }
    
    endpoint = f"/summarize?url={url}&lang=en&engine=2"
    conn.request("GET", endpoint, headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")