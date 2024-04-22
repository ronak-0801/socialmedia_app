from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import get_db,engine, Base
from src.resource.comment.schema import Comment_schema
from src.functionality.comment.add_comment import adding_comment
from src.functionality.comment.delete_comment import deleting_comment

comment_route = APIRouter()
Base.metadata.create_all(bind=engine) 
    

@comment_route.post('/add_comment/{user_id}/{post_id}')
def give_comment(request:Comment_schema,user_id:int,post_id:int,db:session=Depends(get_db)):
    return adding_comment(request,user_id,post_id,db)

@comment_route.delete('/delete_comment/{user_id}/{post_id}')
def delete_comment(user_id:int,post_id:int, db:session=Depends(get_db)):
    return deleting_comment(user_id,post_id,db)