from pydantic import BaseModel, validator

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
