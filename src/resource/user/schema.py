from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

class User_schema(BaseModel):
    name: str
    email: str
    password: str
    gender: Optional[str] = None
    bio: Optional[str] = None
    dob: date


