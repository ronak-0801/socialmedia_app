from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean,Date 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    gender = Column(String)
    bio = Column(String)
    dob = Column(Date)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    posts = relationship('Posts', back_populates="user")

