from pydantic import BaseModel

class Comment_schema(BaseModel):
    comment: str