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

class ReturnMethodEnumeration(Enumeration):
    '''
    Enumerates several types of product return methods.
    '''
    class_: Literal['https://schema.org/ReturnMethodEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnMethodEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
