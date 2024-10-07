from fastapi import APIRouter, status, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session

from src.serializer.user_serializer import UserCreationForm, UserResponseModel, UserResponseModelWithRole
from src.serializer.user_serializer import UpdateUserRoleRequest
from src.models import get_db
from src.models.users_models import User, UserRole
from src.utils.crypto import hash_password
from src.services.user_services import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def create_user(user: UserCreationForm, db: Annotated[Session, Depends(get_db)]):
    new_user = UserService.create_user(user, db)
    return new_user


@router.get("/{user_id}", response_model=UserResponseModel)
def get_user_by_id(user_id: str, db: Annotated[Session, Depends(get_db)]):
    user = UserService.get_user(user_id, db)
    return user


@router.put("/{user_id}/roles", response_model=UserResponseModelWithRole)
def update_user_role(user_id: str, user_roles: UpdateUserRoleRequest, db: Annotated[Session, Depends(get_db)]):
    user = UserService.update_role(user_id, db, user_roles.roles)
    return UserResponseModelWithRole.model_validate(user)