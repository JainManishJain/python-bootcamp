from sqlmodel import Session, create_engine
from typing import Generator

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
