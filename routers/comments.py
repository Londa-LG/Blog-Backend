from typing import List
from database import get_db
from models import Comment_Model
from auth import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter, status, Response
from schema import Comment_Schema, Comment_Response_Single, Comment_Response_Multiple

router = APIRouter(
    tags = ["Comment end-points"]
)

# CRUD endpoints
@router.post("/posts/{post_id}/comments", status_code=status.HTTP_201_CREATED, response_model=Comment_Response_Single)
def Create_Comment(comment_data: Comment_Schema, post_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    comment_data_dic = comment_data.dict()
    comment_data_dic["post_id"] = post_id
    new_comment = Comment_Model(**comment_data_dic)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment

@router.get("/posts/{post_id}/comments", status_code=status.HTTP_200_OK, response_model=List[Comment_Response_Multiple])
def Get_Comments(post_id: int, db: Session = Depends(get_db)):
    comments = db.query(Comment_Model).filter(Comment_Model.post_id == post_id)
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No comments")
    return comments


@router.put("/comments/{comment_id}", status_code=status.HTTP_202_ACCEPTED, response_model=Comment_Response_Single)
def Update_Comment(comment_data: Comment_Schema, comment_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    comment = db.query(Comment_Model).filter(Comment_Model.id == comment_id)
    if not comment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No comment found")
    comment.update(comment_data.dict())
    db.commit()
    return comment.first()

@router.delete("/comments/{comment_id}")
def Delete_Comment(comment_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    comment = db.query(Comment_Model).filter(Comment_Model.id == comment_id)
    if not comment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No comment found")
    comment.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
