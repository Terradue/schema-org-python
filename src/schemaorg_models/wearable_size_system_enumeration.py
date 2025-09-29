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
from .size_system_enumeration import SizeSystemEnumeration

class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    '''
    Enumerates common size systems specific for wearable products.
    '''
    class_: Literal['https://schema.org/WearableSizeSystemEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableSizeSystemEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
