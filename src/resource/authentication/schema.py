from pydantic import BaseModel
from datetime import date
from typing import Optional

class User_schema(BaseModel):
    name: str
    email: str
    password: str
    gender: Optional[str] = None
    bio: Optional[str] = None
    dob: date

class UserLoginSchema(BaseModel):
    username: str
    password: str

class Email_schema(BaseModel):
    email:str
    otp:int


class PasswordResetSchema(BaseModel):
    email: str
    token: str
    new_password: str

class Passwordtokenschema(BaseModel):
    email : str