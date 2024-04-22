from database import Base
from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship

class Follower(Base):
    __tablename__= "follower"
    id = Column(Integer, primary_key=True, index=True)
    followed_to = Column(Integer,ForeignKey('User.id'))  
    following_by = Column(Integer,ForeignKey('User.id')) 

