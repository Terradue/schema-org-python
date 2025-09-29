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

class ReturnFeesEnumeration(Enumeration):
    '''
    Enumerates several kinds of policies for product return fees.
    '''
    class_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnFeesEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
