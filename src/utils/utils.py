from fastapi import Header, HTTPException
import jwt 
import datetime 
from src.config import Config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SECRET_KEY = Config.secrate_key
ALGORITHM = Config.algorithm

'''token creation'''
def create_access_token(user_id):
    try:
        to_encode = {
            "user_id":user_id,
            "token_type":"access"
        }
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        to_encode.update({"exp": expire})
        access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return access_token
    except Exception as e:
        print("Error creating access token:", e)
        raise

def create_refresh_token(user_id):
    try:
        to_encode = {
        "user_id":user_id,
        "token_type":"refresh"
         }
        expire = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        to_encode.update({"exp": expire})
        refresh_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return refresh_token
    except Exception as e:
        print("Error creating refresh token",e)
        raise 
    

def create_access_token_from_refresh_token(user_id):
    try:
        new_access_token = create_access_token(user_id)
        return {"new_access_token": new_access_token}
    except Exception as e:
        print("Eroor in crsting access token from refresh token",e)
        raise




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

'''send mail'''
def send_email(subject: str, body: str, to_email: str):
    try:    
        from_email = Config.from_email
        smtp_server = Config.smtp_server
        smtp_port = Config.smtp_port
        smtp_username = Config.smtp_username
        smtp_password = Config.smtp_password

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
    except Exception as e:
        print("Error sending email:", e)
        raise HTTPException(status_code=500, detail="Failed to send email")

