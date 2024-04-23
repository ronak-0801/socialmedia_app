from fastapi import APIRouter, Depends
from src.resource.login.schema import UserLoginSchema
from database import get_db
from src.functionality.register_user.login import user_login

login_route = APIRouter()

@login_route.post("/login")
def login(form_data:  UserLoginSchema, db = Depends(get_db)):
    return user_login(form_data,db)