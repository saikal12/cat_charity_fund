from datetime import datetime

from pydantic import BaseModel, validator, root_validator, Field
from pydantic import Extra
from typing import Optional


class CharityProjectsBase(BaseModel):
    name: Optional[str] = Field(le=100)
    description: Optional[str]
    full_amount: Optional[str] = Field(0, gt=0)


class CharityProjectsCreate(CharityProjectsBase):
    name: str = Field(..., le=100)
    description: str = Field(...)
    full_amount: str = Field(0, gt=0)


class CharityProjectsUpdate(CharityProjectsBase):
    pass


class CharityProjectsDB(BaseModel):
    name: str = Field(..., le=100)
    description: str = Field(...)
    full_amount: str = Field(0, gt=0)
    id: int = Field(...)
    invested_amount: int = Field(...)
    fully_invested: bool = Field(True)
    create_date: datetime = Field(..., )
    close_date: datetime
