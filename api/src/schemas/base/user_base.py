from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
