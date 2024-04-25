from database import Base
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean,Date 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    gender = Column(String)
    bio = Column(String)
    dob = Column(Date)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    posts = relationship('Posts', back_populates="user")
    is_email_verified = Column(Boolean, default=False)

class Otp(Base):
    __tablename__ = "otp"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    otp = Column(Integer)
    expiration_time = Column(DateTime)

    def is_expired(self):
        return datetime.datetime.now() > self.expiration_time


class PasswordReset(Base):
    __tablename__ = "password_reset"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    token = Column(String, unique=True, index=True)
    expiration_time = Column(DateTime, default=datetime.datetime.utcnow() + datetime.timedelta(hours=1))

    def is_expired(self):
        return datetime.datetime.now() > self.expiration_time


