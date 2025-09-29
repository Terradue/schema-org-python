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

class IncentiveType(Enumeration):
    '''
    Enumerates common financial incentives for products, including tax credits, tax deductions, rebates and subsidies, etc.
    '''
    class_: Literal['https://schema.org/IncentiveType'] = Field( # type: ignore
        default='https://schema.org/IncentiveType',
        alias='@type',
        serialization_alias='@type'
    )
