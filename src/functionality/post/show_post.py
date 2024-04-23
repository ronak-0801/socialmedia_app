
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.resource.post.model import Posts
from src.functionality.register_user.authentication import get_user_id



def post_from_user(user_id:int,db: session=Depends(get_db)):
    posts = db.query(Posts).filter(Posts.uid == user_id).all()
    posts_of_user = []
    for post in posts:
        posts_of_user.append({
            "post": post.post,
            "caption": post.caption,
            "total_like": post.total_like
        })
    return posts_of_user