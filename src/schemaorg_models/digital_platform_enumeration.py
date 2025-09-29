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

class DigitalPlatformEnumeration(Enumeration):
    '''
    Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057). 
    '''
    class_: Literal['https://schema.org/DigitalPlatformEnumeration'] = Field( # type: ignore
        default='https://schema.org/DigitalPlatformEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
