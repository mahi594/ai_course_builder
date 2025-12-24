from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from backend.auth.routes import router as auth_router
from backend.services.course_builder_free import build_course_from_topic

from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

class CourseRequest(BaseModel):
    topic: str
    difficulty: str = "Beginner"

@app.post("/generate-course")
def generate_course(req: CourseRequest):
    return build_course_from_topic(req.topic, req.difficulty)


@app.get("/")
def root():
    return {
        "status": "AI Course Builder backend is running",
        "docs": "/docs"
    }
