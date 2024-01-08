from typing import List
from database import get_db
from utils import pwd_context
from models import User_Model
from auth import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter, status, Response
from schema import User_Schema, User_Response_Single, User_Response_Multiple

router = APIRouter(
    tags = ['User end-points'],
    prefix = "/users"
)

# CRUD functionality

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User_Response_Single)
def Create_User(user_data: User_Schema, db: Session = Depends(get_db)):
    user_data.email = user_data.email.lower()
    hashed_password = pwd_context.hash(user_data.password)
    user_data.password = hashed_password
    new_user = User_Model(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[User_Response_Multiple])
def Get_Users(db: Session = Depends(get_db)):
    users = db.query(User_Model).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users")
    return users

@router.get("/{user_id}", response_model=User_Response_Single)
def Get_User(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User_Model).filter(User_Model.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    return user

@router.put("/{user_id}", status_code=status.HTTP_202_ACCEPTED, response_model=User_Response_Single)
def Update_User(user_id: int, user_data: User_Schema, db: Session = Depends(get_db)):
    user = db.query(User_Model).filter(User_Model.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    hashed_password = pwd_context.hash(user_data.password)
    user_data.password = hashed_password
    user.update(user_data.dict())
    db.commit()
    return user.first()

@router.delete("/{user_id}")
def Delete_User(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User_Model).filter(User_Model.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    user.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
