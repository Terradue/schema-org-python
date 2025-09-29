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
from .enumeration import Enumeration

class IncentiveQualifiedExpenseType(Enumeration):
    '''
    The types of expenses that are covered by the incentive. For example some incentives are only for the goods (tangible items) but the services (labor) are excluded.
    '''
    class_: Literal['https://schema.org/IncentiveQualifiedExpenseType'] = Field( # type: ignore
        default='https://schema.org/IncentiveQualifiedExpenseType',
        alias='@type',
        serialization_alias='@type'
    )
