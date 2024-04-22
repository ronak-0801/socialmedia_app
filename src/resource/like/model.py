from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Like(Base):
    __tablename__ = "Likesofposts"
    id = Column(Integer,primary_key=True,index=True)
    post_user_id = Column(Integer,ForeignKey("Posts.id"))
    like = relationship("Posts", backref="Likesofposts")
    user_id = Column(Integer)