from fastapi import APIRouter, Depends, HTTPException
from database import get_db, engine, Base
from sqlalchemy.orm import session
from src.resource.authentication.model import User
from src.resource.authentication.schema import (
    User_schema,
    UserLoginSchema,
    Email_schema,
    PasswordResetSchema,
    Passwordtokenschema,
)
from src.functionality.authentication.authentication import (
    register_user,
    user_login,
    delete,
    verify_email_with_otp,
    password_reset,
    generate_password_reset_token,
)
from src.utils.utils import (
    create_access_token_from_refresh_token,
    get_user_id_from_refresh_token,
    get_user_id,
)

auth_route = APIRouter()
Base.metadata.create_all(bind=engine)


@auth_route.post("/register_user/")
def registration(request: User_schema, db: session = Depends(get_db)):
    return register_user(request, db)


@auth_route.post("/login")
def login(form_data: UserLoginSchema, db=Depends(get_db)):
    return user_login(form_data, db)


@auth_route.delete("/delete_user")
def delete_user(user_id=Depends(get_user_id), db=Depends(get_db)):
    return delete(user_id, db)


@auth_route.post("/refresh_token")
def generate_token(user_id=Depends(get_user_id_from_refresh_token)):
    return create_access_token_from_refresh_token(user_id)


@auth_route.post("/verify_email")
def verify_email_endpoint(data: Email_schema, db: session = Depends(get_db)):
    email = data.email
    otp = data.otp

    result = verify_email_with_otp(email, otp, db)
    if result["success"]:
        return {
            "message": "Email verified successfully",
            "access_token": result["access_token"],
            "refresh_token": result["refresh_token"],
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid token")


@auth_route.post("/password_reset_token")
def generate_password_token(
    request: Passwordtokenschema, db: session = Depends(get_db)
):
    email = request.email
    return generate_password_reset_token(email, db)


@auth_route.post("/password_reset")
def reset_password(request: PasswordResetSchema, db: session = Depends(get_db)):
    return password_reset(request, db)
