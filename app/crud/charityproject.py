from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from typing import Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.models import CharityProject

class CRUDCharityproject():
    async def get_multi(
            self,
            session: AsyncSession
    ) -> List[CharityProject]:
        db_objs = await session.execute(select(CharityProject))
        return db_objs.scalars().all()

    async def create(
            self,
            obj_in: CharityProjectCreate,
            session: AsyncSession,
    ) -> CharityProject:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
            self,
            session: AsyncSession,
            db_obj: CharityProject,
            obj_in: CharityProjectUpdate,
    ) -> CharityProject:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self,
            session: AsyncSession,
            db_obj: CharityProjectCreate,
    ) -> CharityProjectCreate:
        await session.delete(db_obj)
        await session.commit()
        return db_obj

