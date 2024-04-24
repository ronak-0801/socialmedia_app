from fastapi import FastAPI
from src.resource.authentication.api import auth_route
from src.resource.post.api import post_route
from src.resource.like.api import like_route
from src.resource.comment.api import comment_route
from src.resource.follow.api import follow_route


app = FastAPI()

app.include_router(auth_route)
app.include_router(post_route)
app.include_router(like_route)
app.include_router(comment_route)
app.include_router(follow_route)
