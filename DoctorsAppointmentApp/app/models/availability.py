
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Availability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: int
    start_time: datetime
    end_time: datetime
