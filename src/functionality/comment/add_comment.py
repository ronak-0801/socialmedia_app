from src.resource.comment.schema import Comment_schema
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.resource.post.model import Posts
from src.resource.comment.model import Post_comment



def adding_comment(request:Comment_schema,user_id:int,post_id:int,db:session=Depends(get_db)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    post.comment = {user_id:request.comment}
    comments = Post_comment(comment= request.comment, user_id = user_id,post_id = post_id)
    db.add(comments)
    db.commit()
    db.refresh(comments)

    return "Comments added successfully"