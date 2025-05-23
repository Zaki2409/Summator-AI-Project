# Summator-AI-Project
Teach text summarization and visual storytelling.

This is a simple FastAPI-based API that takes a scene description and additional context, then generates a basic video showing the information as text using OpenCV.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

```
### 2. Run Venv and Install Dependencies:
```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

```
### 23. Running the FastAPI Server 
```
uvicorn main:app --reload
```
### 4.Generate a Video (cURL Command)
```
curl -X POST http://localhost:8000/api/v1/generate-video \
  -H "Content-Type: application/json" \
  -d "{\"scene_description\":\"A lone warrior stands atop a snow-covered mountain\",\"additional_context\":\"Epic fantasy style\"}" \
  --output my_video.mp4
```
### 5. For text summarization (cURL Command)
```
curl "http://localhost:8000/api/v1/summarize?url=https://time.com/6266679/musk-ai-open-letter/"

