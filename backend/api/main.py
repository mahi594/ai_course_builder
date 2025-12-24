from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ----------------------------------
# App initialization (ONLY ONE)
# ----------------------------------
app = FastAPI(
    title="AI Course Builder API",
    version="1.0.0"
)

# ----------------------------------
# CORS (important for frontend)
# ----------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev + deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------
# Root route (FIXES 404 on Render)
# ----------------------------------
@app.get("/")
def root():
    return {
        "status": "AI Course Builder backend is running",
        "docs": "/docs"
    }

# ----------------------------------
# Import routers AFTER app creation
# ----------------------------------
from backend.auth.routes import router as auth_router
from backend.services.course_builder_free import build_course_from_topic

app.include_router(auth_router)

# ----------------------------------
# Request schema
# ----------------------------------
class CourseRequest(BaseModel):
    topic: str
    difficulty: str = "Beginner"

# ----------------------------------
# Generate course
# ----------------------------------
@app.post("/generate-course")
def generate_course(req: CourseRequest):
    try:
        course = build_course_from_topic(
            topic=req.topic,
            difficulty=req.difficulty.lower()
        )
        return course
    except Exception as e:
        print("❌ Course generation error:", e)
        raise HTTPException(status_code=500, detail="Failed to generate course")
