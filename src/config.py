from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    database_url = os.getenv("DATABASE_URL")
    secrate_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    from_email = os.getenv("EMAIL")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
