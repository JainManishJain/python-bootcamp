
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.user import User
from app.models.availability import Availability
from app.models.doctor import Doctor

router = APIRouter()

@router.get("")
def list_doctors(session: Session = Depends(get_session)):
    doctors = session.exec(select(Doctor)).all()
    return doctors

@router.get("/{doctor_id}/availability")
def availability(doctor_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Availability).where(Availability.doctor_id == doctor_id)).all()
