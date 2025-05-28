from pydantic import BaseModel, EmailStr
from typing import Optional


class UserProfileSchema(BaseModel):
    username: str
    firstname: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    age: Optional[int]
    password: Optional[str]

    class Config:
        from_attributes = True


class HouseSchema(BaseModel):
    area: int
    year: int
    garage: int
    total_basement: int
    bath: int
    overall_quality: int
    neighborhood: Optional[str]
    price: Optional[int]

    class Config:
        from_attributes = True