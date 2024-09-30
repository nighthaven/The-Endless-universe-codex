from fastapi import APIRouter, status, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session

from src.serializer.user_serializer import UserCreationForm, UserResponseModel, UserResponseModelWithRole
from src.models import get_db
from src.models.users_models import User, UserRole
from src.utils.crypto import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def create_user(user: UserCreationForm, db: Annotated[Session, Depends(get_db)]):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=UserResponseModel)
def get_user_by_id(user_id: str, db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.put("/{user_id}/roles", response_model=UserResponseModelWithRole)
def update_user_role(user_id: str, roles: List[UserRole], db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.roles = roles
    db.commit()
    db.refresh(user)

    return UserResponseModelWithRole.model_validate(user)