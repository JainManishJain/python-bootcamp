
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from datetime import timedelta, datetime
from app.core.database import get_session
from app.models.appointment import Appointment

router = APIRouter()

@router.post("")
def book(doctor_id: int, patient_id: int, start_time: datetime, session: Session = Depends(get_session)):
    end_time = start_time + timedelta(minutes=30)

    conflict = session.exec(
        select(Appointment).where(
            Appointment.doctor_id == doctor_id,
            Appointment.start_time < end_time,
            Appointment.end_time > start_time
        )
    ).first()

    if conflict:
        raise HTTPException(status_code=400, detail="Slot already booked")

    appt = Appointment(
        doctor_id=doctor_id,
        patient_id=patient_id,
        start_time=start_time,
        end_time=end_time
    )
    session.add(appt)
    session.commit()
    return {"message": "Appointment booked"}
