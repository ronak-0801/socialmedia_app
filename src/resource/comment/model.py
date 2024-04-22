from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,backref

class Post_comment(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True,index=True)
    comment= Column(String)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    cmnt = relationship("Posts", backref="comments")
    user_id = Column(Integer)

