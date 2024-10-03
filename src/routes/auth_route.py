from fastapi import APIRouter, status, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from src.models.users_models import User
from src.models import get_db
from src.serializer.user_serializer import UserResponseModel
from src.utils.Oauth2 import create_access_token
from src.utils.crypto import verify_password

router = APIRouter(
    tags=["authentification"],
)

@router.post("/login")
def login(db: Annotated[Session, Depends(get_db)], request: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token = create_access_token({"user_id": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}