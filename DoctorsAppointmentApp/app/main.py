from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.database import engine
from app.api import auth, doctors, appointments

app = FastAPI(title="DoctorsAppointmentApp")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
