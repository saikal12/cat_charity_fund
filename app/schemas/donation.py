from datetime import datetime, timedelta

from pydantic import BaseModel, validator, root_validator, Field
from pydantic import Extra
from typing import Optional


class DonationBase(BaseModel):
    full_amount: int = Field(..., gt=0)
    comment: str


class DonationDB(DonationBase):
    user_id: int
    invested_amount:int = Field(..., default=0)
    fully_invested: bool = Field(False)
    create_date: datetime = Field(default=datetime.utcnow)
    close_date: datetime


class DonationUser(DonationBase):
    user_id: int
    create_date: datetime = Field(default=datetime.utcnow)


