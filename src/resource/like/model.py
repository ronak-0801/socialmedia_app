from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Boolean,DateTime
from sqlalchemy.orm import relationship

class Like(Base):
    __tablename__ = "Likesofposts"
    id = Column(Integer,primary_key=True,index=True)
    post_user_id = Column(Integer,ForeignKey("Posts.id"))
    like = relationship("Posts", backref="Likesofposts")
    user_id = Column(Integer)
    created_at = Column(DateTime , default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
