from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    database_url = os.getenv("DATABASE_URL")
    secrate_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    access_token_expiration = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))