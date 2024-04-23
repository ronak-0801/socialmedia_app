from src.resource.user.model import User
from src.resource.user.schema import User_schema
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.functionality.register_user.authentication import create_access_token, create_refresh_token
from src.resource.user.model import User
from src.config import Config
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = Config.access_token_expiration


def register_user(request:User_schema,db:session=Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    user = User(name = request.name, email = request.email, password = hashed_password, gender = request.gender,bio=request.bio,dob=request.dob)
    db.add(user)
    db.commit() 
    

    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(user.id)
    
    # refresh_token_expires = timedelta(days=30)  
    refresh_token = create_refresh_token(user.id)
    
    return {"access_token": access_token, "refresh_token":refresh_token}


