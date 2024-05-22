from src.resource.comment.schema import Comment_schema
from sqlalchemy.orm import session
from fastapi import Depends, HTTPException
from database import get_db
from src.resource.post.model import Posts
from src.resource.comment.model import Post_comment
from src.resource.authentication.model import User



def adding_comment(request:Comment_schema,post_id:int,user_id:int,db:session=Depends(get_db)):
    try:
        check_delete = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if check_delete:
            post = db.query(Posts).filter(Posts.id == post_id).first()
            post.comment = {user_id:request.comment}
            comments = Post_comment(comment= request.comment, user_id = user_id,post_id = post_id)
            db.add(comments)
            db.commit()
            db.refresh(comments)

            return "Comments added successfully"    
        else:
            raise HTTPException(status_code=500, detail="Failed to add comment, user is deleted")
    except Exception as e:
        # print("Failed to add comment ",e)
        raise HTTPException(status_code=500, detail="Failed to add comment")
