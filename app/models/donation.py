from cat_charity_fund.app.core.db import Base
from sqlalchemy import Column, Text, Integer, ForeignKey
from .base import BaseModel


class Donation(BaseModel):
    user_id = Column(Integer, ForeignKey('user.id', name='fk_donation_user_id_user'))
    comment = Column(Text)