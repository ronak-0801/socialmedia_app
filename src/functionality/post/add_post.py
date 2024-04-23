from src.resource.post.schema import Post_schema 
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.resource.post.model import Posts
# from src.functionality.register_user.authentication import get_user_id


def add_posts(request:Post_schema ,user_id:int, db: session=Depends(get_db)):
    post = Posts(post = request.post, caption=request.caption, total_like = request.total_like,uid = user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

