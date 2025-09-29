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

class BoardingPolicyType(Enumeration):
    '''
    A type of boarding policy used by an airline.
    '''
    class_: Literal['https://schema.org/BoardingPolicyType'] = Field( # type: ignore
        default='https://schema.org/BoardingPolicyType',
        alias='@type',
        serialization_alias='@type'
    )
