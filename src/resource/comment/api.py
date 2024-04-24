from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import get_db,engine, Base
from src.resource.comment.schema import Comment_schema
from src.functionality.comment.add_comment import adding_comment
from src.functionality.comment.delete_comment import deleting_comment
from src.functionality.authentication.authentication import get_user_id


comment_route = APIRouter()
Base.metadata.create_all(bind=engine) 
    

@comment_route.post('/add_comment/{post_id}')
def give_comment(request:Comment_schema,post_id:int,user_id= Depends(get_user_id),db:session=Depends(get_db)):
    return adding_comment(request,post_id,user_id,db)

@comment_route.delete('/delete_comment/{post_id}')
def delete_comment(post_id:int,user_id= Depends(get_user_id), db:session=Depends(get_db)):
    return deleting_comment(post_id,user_id,db)