from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

from app.database import Base


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]
