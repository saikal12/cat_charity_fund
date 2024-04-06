from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.models import Donation

class CRUDCharityproject():
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
    ) -> Donation:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_user_donation(self,
                                user_id: int,
                                session: AsyncSession) -> List[Donation]:
        user_donation = await session.execute(select(Donation).where(Donation.user_id == user_id))
        return user_donation.scalars().all()



