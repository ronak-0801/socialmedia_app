from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import engine,Base,get_db
from src.functionality.follow.follower import add_follower,show_follower,show_following
from src.utils.utils import get_user_id


follow_route = APIRouter()
Base.metadata.create_all(bind=engine) 

@follow_route.post('/follow/{followed_to}')
def follower( followed_to:int, following_user= Depends(get_user_id),db:session=Depends(get_db)):
    return add_follower(followed_to,following_user,db)

@follow_route.get('/show_follower')
def showing_followers(user_id= Depends(get_user_id), db:session=Depends(get_db)):
    return show_follower(user_id,db)

@follow_route.get('/show_following')
def showing_following(user_id= Depends(get_user_id), db:session=Depends(get_db)):
    return show_following(user_id,db)
