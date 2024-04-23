from fastapi import APIRouter, Depends, HTTPException
from src.resource.user.model import User
from database import get_db
from src.functionality.register_user.authentication import get_user_id


delete_user_route = APIRouter()

@delete_user_route.delete("/delete_user")
def delete_user(user_id= Depends(get_user_id), db = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Soft delete the user
    user.is_active = False
    db.commit()
    return {"message": "User deleted successfully"}
