from fastapi import  Depends, HTTPException,Header
from database import get_db
from sqlalchemy.orm import session
from src.config import Config
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt 
import datetime 
import random
import string
from src.resource.authentication.model import User, Otp
from src.resource.authentication.schema import User_schema
from src.resource.authentication.schema import UserLoginSchema

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SECRET_KEY = Config.secrate_key
ALGORITHM = Config.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = Config.access_token_expiration

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
                raise HTTPException(status_code=403, detail="User account is deactivated")
            
            if not user or not verify_password(form_data.password, user.password):
                raise HTTPException(status_code=401, detail="Incorrect email or password")
            
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            return "User not found"
    except Exception as e:
        print("Error during user login:", e)
        raise HTTPException(status_code=500, detail="Failed to login user")



'''delete'''
def delete(user_id , db = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user.is_deleted = True
        user.is_active = False

        db.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        print("Error deleting user:", e)
        raise HTTPException(status_code=500, detail="Failed to delete user")


'''token creation'''
def create_access_token(user_id):
    to_encode = {
        "user_id":user_id,
        "token_type":"access"
    }
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    to_encode.update({"exp": expire})
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

def create_refresh_token(user_id):
    to_encode = {
        "user_id":user_id,
        "token_type":"refresh"
    }
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    to_encode.update({"exp": expire})
    refresh_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return refresh_token

def create_access_token_from_refresh_token(user_id):
    new_access_token = create_access_token(user_id)
    return {"new_access_token": new_access_token}




'''geting user id from token'''

def get_user_id(authorization: str = Header()):
    try:
        access_token = (authorization).split()[1]
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if payload.get("token_type") == "refresh":
            raise Exception
        return user_id
    except Exception  as e:
        print("JWT decoding error:", e)
        raise HTTPException(status_code=401, detail="unauthorize ")
    
def get_user_id_from_refresh_token(authorization: str = Header()):
    try:
        access_token = (authorization).split()[1]
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        return user_id
    except Exception  as e:
        print("JWT decoding error:", e)
        raise HTTPException(status_code=401, detail="unauthorize ")




'''email-verification'''
def send_email(subject: str, body: str, to_email: str):
    # Configure email settings
    from_email = "ronak285.rejoice@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "ronak285.rejoice@gmail.com"
    smtp_password = "viyabegkjwfvgjkd"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    
    try:
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
    except Exception as e:
        print("Error sending email:", e)
        raise HTTPException(status_code=500, detail="Failed to send email")


def send_verification_email(user_email, otp):
    email_subject = "Email Verification"
    email_body = f"Your OTP for email verification is: {otp}. This OTP will expire in 10 minutes."
    send_email(email_subject, email_body, user_email)

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
                return False
        else:
            return False
    except Exception as e:
        print("Error verifying email with OTP:", e)
        raise HTTPException(status_code=500, detail="Failed to verify email with OTP")
