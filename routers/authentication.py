from schema import Token
from database import get_db
from models import User_Model
from sqlalchemy.orm import Session
from utils import verify_user, create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, APIRouter, status

router = APIRouter(
    tags = ["Authentication end-points"]
)

@router.post("/login", status_code=status.HTTP_200_OK, response_model = Token)
def Login_User(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    credentials.username = credentials.username.lower()
    user = db.query(User_Model).filter(User_Model.email == credentials.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not verify_user(credentials.password, user.password):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token = create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
