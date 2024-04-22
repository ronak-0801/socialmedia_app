from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Post_schema(BaseModel):
    post: str
    caption: str
    total_like: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False




