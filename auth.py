from schema import TokenData
from jose import JWTError, jwt
from utils import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

auth_scheme = OAuth2PasswordBearer(tokenUrl='login')

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token: str = Depends(auth_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers="{'WWW-Authenticate': 'Bearer'}")
    return verify_access_token(token, credentials_exception)
