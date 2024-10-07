from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from src.utils.crypto import hash_password
from src.serializer.user_serializer import UserCreationForm
from typing import List
from src.models.users_models import User, UserRole

class UserService:
    @staticmethod
    def create_user(user_data: UserCreationForm, db: Session) -> User:
        user = db.query(User).filter_by(email=user_data.email).one_or_none()
        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password=hash_password(user_data.password),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_user(user_id, db: Session) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    @staticmethod
    def update_role(user_id, db: Session, roles: List[UserRole]) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.roles = roles
        db.commit()
        db.refresh(user)
        return user