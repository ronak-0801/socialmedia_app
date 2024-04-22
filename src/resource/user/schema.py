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
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False


