from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

load_dotenv()



from backend.services.course_builder_free import build_course_from_topic
from backend.utils.job_store import (
    create_job,
    set_job_result,
    set_job_error,
    get_job
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for local dev
    allow_credentials=True,
    allow_methods=["*"],   # allows OPTIONS, POST, GET
    allow_headers=["*"],
)


# ---------------------------
# Request schema
# ---------------------------
class CourseRequest(BaseModel):
    topic: str
    difficulty: str = "beginner"
    videos_per_topic: int = 1


# ---------------------------
# Home
# ---------------------------
@app.get("/")
def home():
    return {"status": "AI Course Builder API running"}


# ---------------------------
# Background task
# ---------------------------
def run_course_job(job_id: str, req: CourseRequest):
    try:
        course = build_course_from_topic(
            topic=req.topic,
            difficulty=req.difficulty,
            videos_per_topic=req.videos_per_topic
        )
        set_job_result(job_id, course)
    except Exception as e:
        set_job_error(job_id, e)


# ---------------------------
# Generate course
# ---------------------------
@app.post("/generate-course")
def generate_course(request: CourseRequest):
    course = build_course_from_topic(
        topic=request.topic,
        difficulty=request.difficulty
    )
    return course



# ---------------------------
# Job status
# ---------------------------
@app.get("/status/{job_id}")
def job_status(job_id: str):
    job = get_job(job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job
