from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey,DateTime,Boolean


class Follower(Base):
    __tablename__= "follower"
    id = Column(Integer, primary_key=True, index=True)
    followed_to = Column(Integer,ForeignKey('User.id'))  
    following_by = Column(Integer,ForeignKey('User.id')) 
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime , default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

