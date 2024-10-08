from fastapi import status, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from typing import List
from src.models.users_models import User, UserRole
from src.models import get_db

class UserService:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db


    def create_user(self, user_data: User) -> User:
        user = self.db.query(User).filter_by(email=user_data.email).one_or_none()
        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        self.db.add(user_data)
        self.db.commit()
        self.db.refresh(user_data)
        return user_data


    def get_user(self, email: str) -> User:
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user


    def update_role(self, email: str, roles: List[UserRole]) -> User:
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.roles = roles
        self.db.commit()
        self.db.refresh(user)
        return user