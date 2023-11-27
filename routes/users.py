import os
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from models.users import User, TokenResponse

from auth.hash_password import HashPassword
from database.connection import Database

user_router = APIRouter(
    tags=["User"],
)

templates = Jinja2Templates(directory="templates")
# BASE_DIR = os.path.dirname(os.path.realpath("__file__"))
# templates.env.globals["STATIC_URL"] = "/static"
# user_router.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already"
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {
        "message": "User created successfully."
    }

@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(response: Response, request: Request, user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist"
        )
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        response.set_cookie(key="token",value=access_token,httponly=True)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
    # templates.TemplateResponse("users.html",{
    #     "request":request,
    #     "username":user.username,
    #     # "BASE_DIR":BASE_DIR,
    # })
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid details passed"
    )
