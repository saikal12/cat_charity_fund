from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.donation import DonationCreate

from app.core.db import Base
from app.models import Donation, User


class DonationCRUD():
    async def get_multi(
            self,
            session: AsyncSession
    ) -> List[Donation]:
        db_objs = await session.execute(select(Donation))
        return db_objs.scalars().all()

    async def create(
            self,
            obj_in: DonationCreate,
            session: AsyncSession,
            user: User
    ) -> Donation:
        obj_in_data = obj_in.dict()
        obj_in_data['user_id'] = user.id
        db_obj = Donation(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_user_donation(self,
                                user_id: int,
                                session: AsyncSession) -> List[Donation]:
        user_donation = await session.execute(select(Donation).where(Donation.user_id == user_id))
        return user_donation.scalars().all()


donation_crud = DonationCRUD()