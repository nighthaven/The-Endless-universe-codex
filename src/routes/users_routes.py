from fastapi import APIRouter, status, Depends
from typing import Annotated, Any

from src.serializer.user_serializer import UserCreationForm, UserResponseModel, UserResponseModelWithRole
from src.serializer.user_serializer import UpdateUserRoleRequest
from src.models.users_models import User
from src.utils.crypto import hash_password
from src.services.user_services import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def create_user(user_service: Annotated[Any, Depends(UserService)], user: UserCreationForm):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )
    new_user = user_service.create_user(new_user)
    return new_user


@router.get("/{email}", response_model=UserResponseModel)
def get_user_by_email(user_service: Annotated[Any, Depends(UserService)], email: str):
    user = user_service.get_user(email)
    return user


@router.put("/{email}/roles", response_model=UserResponseModelWithRole)
def update_user_role(user_service: Annotated[Any, Depends(UserService)], email: str, user_roles: UpdateUserRoleRequest):
    user = user_service.update_role(email, user_roles.roles)
    return UserResponseModelWithRole.model_validate(user)