from typing import Annotated, Any

from fastapi import APIRouter, Depends, status
from src.models.users_models import User
from src.repositories.user_repository import UserRepository
from src.schemas.form_creation.user_form_creation import UserCreationForm
from src.schemas.form_creation.user_form_update import UserFormUpdate
from src.schemas.response.user_response import UserResponse
from src.schemas.response.user_response_with_role import UserResponseModelWithRole
from src.utils.crypto import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(
    user_repository: Annotated[Any, Depends(UserRepository)], user: UserCreationForm
) -> User:
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )
    new_user = user_repository.save_user(new_user)
    return new_user


@router.get("/{email}", response_model=UserResponse)
def get_user_by_email(
    user_repository: Annotated[UserRepository, Depends(UserRepository)], email: str
) -> User:
    user = user_repository.get_user_by_email(email)
    return user


@router.put("/{email}/roles", response_model=UserResponseModelWithRole)
def update_user_role(
    user_repository: Annotated[UserRepository, Depends(UserRepository)],
    email: str,
    user_roles: UserFormUpdate,
) -> UserResponseModelWithRole:
    user = user_repository.update_role(email, user_roles.roles)
    return UserResponseModelWithRole.model_validate(user)
