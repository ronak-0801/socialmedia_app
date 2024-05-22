from fastapi import  Depends, HTTPException
from database import get_db
from sqlalchemy.orm import session
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import datetime 
import random
import string
from src.resource.authentication.model import User, Otp, PasswordReset
from src.resource.authentication.schema import User_schema
from src.resource.authentication.schema import UserLoginSchema,PasswordResetSchema
from src.utils.utils import create_access_token, create_refresh_token,send_email



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))


'''user registration'''
def register_user(request:User_schema,db:session=Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == request.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email address already registered")
        
        hashed_password = pwd_context.hash(request.password)
        user = User(name=request.name, email=request.email, password=hashed_password, gender=request.gender, bio=request.bio, dob=request.dob)

        db.add(user)
        
        otp = generate_otp()
        expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
        db_otp = Otp(email=request.email, otp=otp, expiration_time=expiration_time)
        db.add(db_otp)

        db.commit() 

        send_verification_email(request.email, otp)

        return {"message": "User registered. Verification email sent."}
    
    except Exception as e:
        print("Error registering user:", e)
        raise HTTPException(status_code=500, detail="Failed to register user")




'''user login'''
def user_login(form_data: UserLoginSchema, db = Depends(get_db)):

    try:
        user = db.query(User).filter(User.name == form_data.username, User.is_deleted == False).first()
        if user:
            if not user.is_active:
                return HTTPException(status_code=403, detail="User account is deactivated")
            
            if not user or not verify_password(form_data.password, user.password):
                return HTTPException(status_code=401, detail="Incorrect email or password")
            
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            raise  "User not found" 
    except Exception as e:
        print("Error during user login:", e)
        raise HTTPException(status_code=500, detail="Failed to login user")



'''delete'''
def delete(user_id , db = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if user:

            user.is_deleted = True
            user.is_active = False

            db.commit()
            return {"message": "User deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")  
    except Exception as e:
        print("Error deleting user:", e)
        raise HTTPException(status_code=500, detail="Failed to delete user")
    
    

'''email-verification'''

def send_verification_email(user_email, otp):
    try:
        email_subject = "Email Verification"
        email_body = f"Your OTP for email verification is: {otp}. This OTP will expire in 10 minutes."
        send_email(email_subject, email_body, user_email)
    except Exception as e:
        print("Error sending verification email:", e)
        raise

def verify_email_with_otp(email: str, otp: str, db: session):
    try:
        user_otp = db.query(Otp).filter(Otp.email == email, Otp.otp == otp).first()

        if user_otp and not user_otp.is_expired():
            user = db.query(User).filter(User.email == email).first()
            if user:
                user.is_email_verified = True
                user.is_active = True
                access_token = create_access_token(user.id) 
                refresh_token = create_refresh_token(user.id)
                db.delete(user_otp)
                db.commit()
                return {"success": True, "access_token": access_token, "refresh_token": refresh_token}
            else:
                return {"success":False}
        else:
            raise HTTPException
    except Exception as e:
        print("Error verifying email with OTP:", e)
        raise HTTPException(status_code=500, detail="Failed to verify email with OTP")
    




    

'''Password reset'''
def password_reset(request: PasswordResetSchema, db: session = Depends(get_db)):
    try:
        email = request.email
        token = request.token
        new_password = request.new_password
        
        password_reset = db.query(PasswordReset).filter(PasswordReset.email == email, PasswordReset.token == token).first()
        if password_reset and not password_reset.is_expired():
            user = db.query(User).filter(User.email == email).first()
            if user:
                hashed_password = pwd_context.hash(new_password)
                user.password = hashed_password
                db.delete(password_reset)
                db.commit()
                return {"message": "Password reset successfully"}
            else:
                raise HTTPException(status_code=404, detail="User not found")
        else:
            raise HTTPException(status_code=400, detail="Invalid or expired token")
    except Exception as e:
        print("Error resetting password:", e)
        raise HTTPException(status_code=500, detail="Failed to reset password")


def generate_password_reset_token(email: str, db: session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            token = create_access_token(user.id)
            expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1)
            password_reset = PasswordReset(email=email, token=token, expiration_time=expiration_time)
            db.add(password_reset)
            db.commit()
            send_password_reset_email(email, token)
            return {"message": "Password reset email sent successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        print("Error generating password reset token:", e)
        raise HTTPException(status_code=500, detail="Failed to generate password reset token")

def send_password_reset_email(email: str, token: str):
    try:
        email_subject = "Password Reset"
        email_body = f"Your token for reseting password: {token}"
        send_email(email_subject, email_body, email)
    except Exception as e:
        print("Error sending password reset email:", e)
        raise HTTPException(status_code=500, detail="Failed to send password reset email")




