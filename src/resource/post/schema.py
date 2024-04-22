from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Post_schema(BaseModel):
    post: str
    caption: str
    total_like: int

