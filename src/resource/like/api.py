from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from database import get_db,engine, Base
from src.functionality.like.add_remove_like import add_like

like_route = APIRouter()
Base.metadata.create_all(bind=engine) 

@like_route.post('/addlike/{user_id}/{post_id}')
def give_like(user_id:int,post_id:int ,db:session=Depends(get_db)):
    return add_like(user_id,post_id,db)



