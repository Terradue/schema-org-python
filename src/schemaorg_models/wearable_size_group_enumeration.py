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
from .size_group_enumeration import SizeGroupEnumeration

class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    '''
    Enumerates common size groups (also known as "size types") for wearable products.
    '''
    class_: Literal['https://schema.org/WearableSizeGroupEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableSizeGroupEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
