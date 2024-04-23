from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import get_db,engine, Base
from src.functionality.like.add_remove_like import add_like
from src.functionality.register_user.authentication import get_user_id

like_route = APIRouter()
Base.metadata.create_all(bind=engine) 

@like_route.post('/addlike/{post_id}')
def give_like(post_id:int ,user_id= Depends(get_user_id),db:session=Depends(get_db)):
    return add_like(post_id,user_id,db)



