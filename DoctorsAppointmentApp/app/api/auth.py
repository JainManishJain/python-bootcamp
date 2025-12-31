
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest
from app.core.security import hash_password, verify_password, create_token
from app.models.doctor import Doctor

router = APIRouter()

@router.post("/register")
def register(data: RegisterRequest, session: Session = Depends(get_session)):
    user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        role=data.role.capitalize(),
        name=data.name
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    
    if data.role == "Doctor":
        doctor = Doctor(
            user_id=user.id,
            name=data.name
        )
        session.add(doctor)
        session.commit()

    return {"message": "User registered"}


@router.post("/login")
def login(data: LoginRequest, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == data.email)).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": create_token({"sub": user.email}, 60),
        "refresh_token": create_token({"sub": user.email}, 1440)
    }

@router.post("/forgot-password")
def forgot_password(email: str):
    return {"message": "Mock reset flow"}
