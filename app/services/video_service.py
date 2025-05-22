from app.utils.http_client import make_video_api_request

def generate_video_prompt(scene_description, additional_context):
    payload = {
        "sceneDescription": scene_description,
        "additionalContext": additional_context
    }
    return make_video_api_request(payload)