from fastapi import  Depends, HTTPException
from src.functionality.register_user.authentication import create_access_token
from src.resource.user.model import User
from src.functionality.register_user.authentication import verify_password
from src.resource.login.schema import UserLoginSchema
from database import get_db



def user_login(form_data:  UserLoginSchema, db = Depends(get_db)):

    user = db.query(User).filter(User.name == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    if not user.is_active:
        raise HTTPException(status_code=403, detail="User account is deactivated")

    access_token = create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

