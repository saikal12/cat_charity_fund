from sqlalchemy import Column, Text, Integer, ForeignKey
from .base import BaseModel
from ..core.db import Base


class Donation(Base, BaseModel):
    user_id = Column(Integer, ForeignKey('user.id', name='fk_donation_user_id_user'))
    comment = Column(Text)