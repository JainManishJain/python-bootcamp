from fastapi import FastAPI
from .database import Base, engine
from .routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Login Management Service")
app.include_router(auth.router)
