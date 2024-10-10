from typing import Annotated, Any

from fastapi import APIRouter, Depends, status

from src.models.users_models import User
from src.serializer.user_serializer import (
    UpdateUserRoleRequest,
    UserCreationForm,
    UserResponseModel,
    UserResponseModelWithRole,
)
from src.services.user_services import UserService
from src.utils.crypto import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def create_user(
    user_service: Annotated[Any, Depends(UserService)], user: UserCreationForm
) -> User:
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )
    new_user = user_service.create_user(new_user)
    return new_user


@router.get("/{email}", response_model=UserResponseModel)
def get_user_by_email(
    user_service: Annotated[UserService, Depends(UserService)], email: str
) -> User:
    user = user_service.get_user_by_email(email)
    return user


@router.put("/{email}/roles", response_model=UserResponseModelWithRole)
def update_user_role(
    user_service: Annotated[UserService, Depends(UserService)],
    email: str,
    user_roles: UpdateUserRoleRequest,
) -> UserResponseModelWithRole:
    user = user_service.update_role(email, user_roles.roles)
    return UserResponseModelWithRole.model_validate(user)
