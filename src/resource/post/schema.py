from pydantic import BaseModel

class Post_schema(BaseModel):
    post: str
    caption: str
    total_like: int

