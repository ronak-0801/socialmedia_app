from src.resource.like.model import Like
from src.resource.post.model import Posts
from sqlalchemy.orm import session
from fastapi import Depends, HTTPException
from database import get_db
from src.resource.authentication.model import User


def add_like(post_id:int,user_id:int ,db:session=Depends(get_db)):
    
    try:
        post = db.query(Posts).filter(Posts.id == post_id).first()
        user = post.id
        post_like = db.query(Like).filter(Like.user_id == user_id , Like.post_user_id == post_id).first()
        check_delete = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if check_delete:
            if post_like:
                db.query(Like).filter(Like.user_id == user_id, Like.post_user_id == post_id).delete()
                post.total_like -= 1
                db.commit()
                return {"post": "post is unliked"}
            else:    
                like = Like(user_id = user_id,post_user_id = user)
                db.add(like)
                post.total_like += 1
                db.commit()
                db.refresh(like)
                return {"post":"post is liked"}
        else:
            raise Exception 
    except Exception as e:
        print("failed to like",e)
        raise HTTPException(status_code=500, detail="user not found ")
    


    