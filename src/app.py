from fastapi import FastAPI
from src.resource.user.api import user_route
from src.resource.post.api import post_route
from src.resource.like.api import like_route
from src.resource.comment.api import comment_route
from src.resource.follow.api import follow_route
from src.resource.login.api import login_route

app = FastAPI()

app.include_router(user_route)
app.include_router(post_route)
app.include_router(like_route)
app.include_router(comment_route)
app.include_router(follow_route)
app.include_router(login_route)