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

class StatusEnumeration(Enumeration):
    '''
    Lists or enumerations dealing with status types.
    '''
    class_: Literal['https://schema.org/StatusEnumeration'] = Field( # type: ignore
        default='https://schema.org/StatusEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
