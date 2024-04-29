from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean , ForeignKey
from sqlalchemy.orm import relationship

class Posts(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True, index=True)
    post = Column(String)
    caption = Column(String)
    total_like = Column(Integer)
    uid = Column(Integer, ForeignKey('User.id'))
    user = relationship("User", back_populates="posts")
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime , default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())



