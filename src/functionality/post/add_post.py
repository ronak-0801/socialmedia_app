from src.resource.post.schema import Post_schema 
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.resource.post.model import Posts
from src.resource.authentication.model import User


def add_posts(request:Post_schema ,user_id:int, db: session=Depends(get_db)):
    
    try:
        user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if user:
            post = Posts(post = request.post, caption=request.caption, total_like = request.total_like,uid = user_id)
            db.add(post)
            db.commit()
            db.refresh(post)
            return post
        else :
            return "User is deleted"

    except Exception as e:
        print("Error in adding the post ",e)
        raise

