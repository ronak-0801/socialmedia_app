
from sqlalchemy.orm import session
from fastapi import Depends, HTTPException
from database import get_db
from src.resource.post.model import Posts
from src.resource.authentication.model import User


def post_from_user(user_id:int,db: session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if user:
            posts = db.query(Posts).filter(Posts.uid == user_id).all()
            posts_of_user = []
            for post in posts:
                posts_of_user.append({
                    "post": post.post,
                    "caption": post.caption,
                    "total_like": post.total_like
                })
            return posts_of_user
        else :
            raise Exception 
    except Exception as e:
        print("error showing post",e)
        raise HTTPException(status_code=500, detail="Failed to show post")
    

