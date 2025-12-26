from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.db.database import SessionLocal
from backend.db.models import User
from backend.auth.utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# --------------------
# DB Dependency
# --------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------
# Request Schemas
# --------------------
class AuthRequest(BaseModel):
    email: str
    password: str

# --------------------
# Signup
# --------------------
@router.post("/signup")
def signup(req: AuthRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == req.email).first():
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        email=req.email,
        hashed_password=hash_password(req.password)
    )
    db.add(user)
    db.commit()

    return {"message": "User created successfully"}

# --------------------
# Login
# --------------------
@router.post("/login")
def login(req: AuthRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == req.email).first()

    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
