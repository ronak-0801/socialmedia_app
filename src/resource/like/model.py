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
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime , default=datetime)
    updated_at = Column(DateTime, default=datetime)