from fastapi import Depends
from sqlalchemy.orm import session
from database import get_db
from src.resource.follow.model import Follower
from src.resource.authentication.model import User

def add_follower( followed_to:int,following_user:int, db:session=Depends(get_db)):
    follower = Follower(followed_to= followed_to,following_by = following_user)

    db.add(follower) 
    db.commit()
    return "successfully followed user"
    
    
    
def show_follower(user_id:int, db:session=Depends(get_db)):
    count_follower = db.query(Follower).filter(Follower.followed_to == user_id).count()
    list_follower = db.query(Follower).filter(Follower.followed_to == user_id).all()
    list_of_follower= []

    for follower in list_follower:
        list_of_follower.append(db.query(User).filter(User.id == follower.following_by).first())
    return  {"number_of_followers":count_follower,
             "follower list":list_of_follower}

def show_following(user_id:int, db:session=Depends(get_db)):
    count_following = db.query(Follower).filter(Follower.following_by == user_id).count()
    following = db.query(Follower).filter(Follower.following_by == user_id).all()
    list_of_follower= []

    for follower in following:
        list_of_follower.append(db.query(User).filter(User.id == follower.followed_to).first())
    return  {"number_of_followers":count_following,
             "following list":list_of_follower}
    


