from app.utils.http_client import make_video_api_request
import requests
from app.config import Config
#from moviepy import TextClip, concatenate_videoclips
import textwrap
import os
from datetime import datetime
from app.config import Config
import cv2
import numpy as np


def generate_video_prompt(scene_description, additional_context):
    payload = {
        "sceneDescription": scene_description,
        "additionalContext": additional_context
    }
    return make_video_api_request(payload)


def generate_actual_video(prompt_data):
    """Convert JSON scene data into MP4 video using OpenCV"""
    try:
        os.makedirs("video_outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"video_outputs/output_{timestamp}.mp4"
        
        # Video settings
        frame_size = (720, 480)
        fps = 24
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

        # Helper function to create text frames
        def create_text_frame(text, duration_sec):
            frames = int(fps * duration_sec)
            for _ in range(frames):
                frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
                y = 50
                for line in textwrap.wrap(text, width=40):
                    cv2.putText(frame, line, (50, y), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                               (255, 255, 255), 2, cv2.LINE_AA)
                    y += 40
                out.write(frame)

        # Title frame
        create_text_frame("Scene Visualization", 3)

        # Setting frame
        create_text_frame(prompt_data['sceneDetails']['setting'], 5)

        # Visual style frame
        create_text_frame(prompt_data['sceneDetails']['visualStyle'], 5)

        # Technical details frame
        tech_details = [
            f"Camera: {prompt_data['promptVariations'][0]['technicalDetails']['cameraAngles']}",
            f"Lighting: {prompt_data['promptVariations'][0]['technicalDetails']['lighting']}",
            f"Movement: {prompt_data['promptVariations'][0]['technicalDetails']['movements']}"
        ]
        create_text_frame("\n".join(tech_details), 7)

        out.release()

        return {
            "status": "success",
            "video_path": output_path,
            "prompt_used": prompt_data['promptVariations'][0]['prompt']
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "error_type": type(e).__name__
        }