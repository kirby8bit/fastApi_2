from typing import List
from fastapi import APIRouter
from tables import Operation as tableOperation
from models.operations import Operation
from database import Session


router = APIRouter(
    prefix ='/operations',
)

@router.get('/',response_model=List[Operation])
def get_operations():
    session = Session()
    operations = (
        session
        .query(tableOperation)
        .all()
    )
    return operations