from pydantic import BaseModel, validator
from datetime import datetime

from src.enums.user_enums import UserErrors


class UserCreateResponse(BaseModel):
    id: int
    username: str
    email: str

    @validator("email")
    def validate_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)


class UserDataResponse(BaseModel):
    id: int
    username: str
    last_login: datetime


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
