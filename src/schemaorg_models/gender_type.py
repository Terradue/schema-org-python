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

class GenderType(Enumeration):
    '''
    An enumeration of genders.
    '''
    class_: Literal['https://schema.org/GenderType'] = Field( # type: ignore
        default='https://schema.org/GenderType',
        alias='@type',
        serialization_alias='@type'
    )
