from src.resource.post.schema import Post_schema 
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.resource.post.model import Posts


def add_posts(user_id:int, request:Post_schema , db: session=Depends(get_db)):
    post = Posts(post = request.post, caption=request.caption, total_like = request.total_like,created_at = request.created_at,updated_at = request.updated_at, is_active= request.is_active, is_deleted = request.is_deleted,uid = user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

