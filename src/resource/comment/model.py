from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,DateTime
from sqlalchemy.orm import relationship

class Post_comment(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True,index=True)
    comment= Column(String)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    cmnt = relationship("Posts", backref="comments")
    user_id = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime , default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

