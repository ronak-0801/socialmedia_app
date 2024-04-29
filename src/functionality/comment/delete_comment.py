
from src.resource.post.model import Posts
from src.resource.comment.model import Post_comment
from sqlalchemy.orm import session
from fastapi import Depends
from database import get_db
from src.resource.authentication.model import User



def deleting_comment(comment_id:int,user_id:int, db:session=Depends(get_db)):
    try:
        check_delete = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        if check_delete:
            comment = db.query(Post_comment).filter(Post_comment.id == comment_id).first()
            if comment :
                if comment.user_id == user_id:
                    db.delete(comment)
                    db.commit()
                
                    return "Comment deleted by comment user" 
                else:

                    user_id_ofpost = db.query(Posts).filter(Posts.id == comment.post_id).first()
                    if user_id_ofpost:
                        if user_id_ofpost.uid == user_id:
                            db.delete(comment)
                            db.commit()
                            return "Comment deleted by post user"
                        else:
                            return "User of post not exist"
                    else:
                        return "Post not exist"
            else:
                return "comment does not exist for deleting"
        else:
            return "User is deleted"
    except Exception as e:
        print("error in deleting comment",e)
        raise




            