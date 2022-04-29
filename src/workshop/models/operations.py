from decimal import Decimal
from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional

class OperationKind(str,Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(BaseModel):
    class Config:
        orm_mode = True
    id: int
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]