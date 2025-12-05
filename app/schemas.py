from pydantic import BaseModel

class PostCreate(BaseModel):
    id: int
    title: str

class PostResponse(BaseModel):
    id: int
    title: str