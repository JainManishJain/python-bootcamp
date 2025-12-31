from typing import Optional
from sqlmodel import SQLModel, Field

class Doctor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    name: str
    specialization: Optional[str] = None
