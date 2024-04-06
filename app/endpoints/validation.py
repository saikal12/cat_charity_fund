from sqlalchemy import select

from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.reservation import reservation_crud
from app.core.user import current_superuser, current_user
from app.crud.meeting_room import meeting_room_crud
from app.models import User, Donation


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await session.execute(
            select(Donation.id).where(
                Donation.name == project_name
            )
        )
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!"',
        )


