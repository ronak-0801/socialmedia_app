from fastapi import APIRouter, Depends
from database import get_db,engine,Base
from sqlalchemy.orm import session
from src.resource.user.schema import User_schema
from src.functionality.register_user.user_registration import register_user


user_route = APIRouter()

Base.metadata.create_all(bind=engine)   

@user_route.post("/register_user/")
def registration(request:User_schema,db:session= Depends(get_db)):
    return register_user(request,db)
