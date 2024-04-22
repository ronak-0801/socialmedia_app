from src.resource.user.model import User
from src.resource.user.schema import User_schema
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db

def register_user(request:User_schema,db:session=Depends(get_db)):
    user = User(name = request.name, email = request.email, password = request.password, gender = request.gender,bio=request.bio,dob=request.dob)
    db.add(user)
    db.commit() 
    db.refresh(user)
    return user