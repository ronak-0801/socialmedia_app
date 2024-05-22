from fastapi import Depends, HTTPException
from sqlalchemy.orm import session
from database import get_db
from src.resource.follow.model import Follower
from src.resource.authentication.model import User

def add_follower( followed_to:int,following_user:int, db:session=Depends(get_db)):
    try:
        check_delete = db.query(User).filter(User.id == following_user, User.is_deleted == False).first()
        if check_delete:
            follower = Follower(followed_to= followed_to,following_by = following_user)

            db.add(follower) 
            db.commit()
            return "successfully followed user"
        else:
            raise Exception 
    except Exception as e:
        print("Failed to follow",e)
        raise HTTPException(status_code=500, detail="Failed to follow user")
        
def show_follower(user_id:int, db:session=Depends(get_db)):
    
    try:
        check_delete = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if check_delete:
            count_follower = db.query(Follower).filter(Follower.followed_to == user_id).count()
            list_follower = db.query(Follower).filter(Follower.followed_to == user_id).all()
            list_of_follower= []

            for follower in list_follower:
                list_of_follower.append(db.query(User).filter(User.id == follower.following_by).first())
            return  {"number_of_followers":count_follower,
                    "follower list":list_of_follower}
        else:
            raise Exception 
    except Exception as e:
        print("error showing follower",e)
        raise HTTPException(status_code=500, detail="Failed to show follower")
    

def show_following(user_id:int, db:session=Depends(get_db)):
    try:
        check_delete = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if check_delete:
            count_following = db.query(Follower).filter(Follower.following_by == user_id).count()
            following = db.query(Follower).filter(Follower.following_by == user_id).all()
            list_of_follower= []

            for follower in following:
                list_of_follower.append(db.query(User).filter(User.id == follower.followed_to).first())
            return  {"number_of_followings": count_following,
                    "following list":list_of_follower}
        else:
            raise Exception 
    except Exception as e:
        print("error showing follower",e)
        raise HTTPException(status_code=500, detail="Failed to show following")
    


