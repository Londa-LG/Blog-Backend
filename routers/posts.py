from typing import List
from database import get_db
from models import Post_Model
from auth import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter, status, Response
from schema import Post_Schema, Post_Response_Single, Post_Response_Multiple

router = APIRouter(
    tags = ['Post end-points'],
    prefix = "/posts"
)

#CRUD functionality
@router.post("/", response_model=Post_Response_Single)
def Create_Post(post_data: Post_Schema, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    post_data.category = post_data.category.upper()
    new_post = Post_Model(**post_data.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/", response_model=List[Post_Response_Multiple])
def Get_Posts(db: Session = Depends(get_db)):
    posts = db.query(Post_Model).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    return posts

@router.get("/{post_id}", response_model=Post_Response_Single)
def Get_Post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post_Model).filter(Post_Model.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found")
    return post

@router.put("/{post_id}", response_model=Post_Response_Single)
def Update_Post(post_id: int, post_data: Post_Schema, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    post_data.category = post_data.category.upper()
    post = db.query(Post_Model).filter(Post_Model.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found")
    post.update(post_data.dict())
    db.commit()
    return post.first()

@router.delete("/{post_id}")
def Delete_Post(post_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    post = db.query(Post_Model).filter(Post_Model.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post found")
    post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
