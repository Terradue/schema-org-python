from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .financial_service import FinancialService

class AutomatedTeller(FinancialService):
    '''
    ATM/cash machine.
    '''
    class_: Literal['https://schema.org/AutomatedTeller'] = Field( # type: ignore
        default='https://schema.org/AutomatedTeller',
        alias='@type',
        serialization_alias='@type'
    )
