from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)


class CRUDCharityproject(
        CRUDBase[CharityProject, CharityProjectCreate, CharityProjectUpdate]):
    pass


charity_project_crud = CRUDCharityproject(CharityProject)
