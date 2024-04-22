from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import get_db,engine, Base
from src.resource.post.schema import Post_schema
from src.functionality.post.add_post import add_posts
from src.functionality.post.show_post import post_from_user

post_route = APIRouter()
Base.metadata.create_all(bind=engine) 


@post_route.post('/addpost/{user_id}')
def addposts(user_id:int, request:Post_schema , db: session=Depends(get_db)):
    return add_posts(user_id,request , db)

@post_route.get('/allpost/{user_id}')
def show_post_from_user(user_id :int,db: session=Depends(get_db)):
    return post_from_user(user_id,db)



