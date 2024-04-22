from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import engine,Base,get_db
from src.functionality.follow.follower import add_follower,show_follower,show_following

follow_route = APIRouter()
Base.metadata.create_all(bind=engine) 

@follow_route.post('/follow/{following_user}/{followed_to}')
def follower(following_user:int, followed_to:int, db:session=Depends(get_db)):
    return add_follower(following_user,followed_to,db)

@follow_route.get('/show_follower/{user_id}')
def showing_followers(user_id:int, db:session=Depends(get_db)):
    return show_follower(user_id,db)

@follow_route.get('/show_following/{user_id}')
def showing_following(user_id:int, db:session=Depends(get_db)):
    return show_following(user_id,db)
