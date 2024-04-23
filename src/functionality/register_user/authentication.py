from src.config import Config
from fastapi import Depends , HTTPException, Header
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt 

import datetime 

SECRET_KEY = Config.secrate_key
ALGORITHM = Config.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = Config.access_token_expiration

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


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



def get_user_id(authorization: str = Header()):

    try:
        access_token = (authorization).split()[1]
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if payload.get("token_type") == "refresh":
            raise Exception
        return user_id
    except Exception  as e:
        print("JWT decoding error:", e)
        raise HTTPException(status_code=401, detail="unauthorize ")

