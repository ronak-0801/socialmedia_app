from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import get_db,engine, Base
from src.resource.post.schema import Post_schema
from src.functionality.post.add_post import add_posts
from src.functionality.post.show_post import post_from_user
from src.utils.utils import get_user_id

post_route = APIRouter()
Base.metadata.create_all(bind=engine) 


@post_route.post('/addpost')
def addposts(request:Post_schema , user_id= Depends(get_user_id), db: session=Depends(get_db)):
    return add_posts(request, user_id , db)

@post_route.get('/allpost')
def show_post_from_user(user_id:int=Depends(get_user_id),db: session=Depends(get_db)):
    return post_from_user(user_id,db)



