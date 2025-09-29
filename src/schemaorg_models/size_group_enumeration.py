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

class SizeGroupEnumeration(Enumeration):
    '''
    Enumerates common size groups for various product categories.
    '''
    class_: Literal['https://schema.org/SizeGroupEnumeration'] = Field( # type: ignore
        default='https://schema.org/SizeGroupEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
