from datetime import datetime

from pydantic import BaseModel, validator, root_validator, Field, PositiveInt
from pydantic import Extra
from typing import Optional


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[int] = Field(gt=0)

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(...)
    full_amount: int = Field(gt=0)


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
