from typing import Optional
from pydantic import BaseModel, EmailStr

class Post_Schema(BaseModel):
    id: int
    title: str
    content: str
    category: str
    created_updated: str
    author: str

class Post_Response_Single(BaseModel):
    id: int
    title: str
    content: str
    category: str
    created_updated: str
    author: str

class Post_Response_Multiple(BaseModel):
    id: int
    title: str

class User_Schema(BaseModel):
    id: int
    admin: bool
    username: str
    email: EmailStr
    password: str

class User_Response_Single(BaseModel):
    id: int
    username: str
    email: EmailStr

class User_Response_Multiple(BaseModel):
    id: int
    username: str

class Comment_Schema(BaseModel):
    id: int
    content: str
    author: str
    date_created: str

class Comment_Response_Single(BaseModel):
    id: int
    content: str
    author: str
    date_created: str

class Comment_Response_Multiple(BaseModel):
    id: int
    content: str
    author: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]
