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

class AdultOrientedEnumeration(Enumeration):
    '''
    Enumeration of considerations that make a product relevant or potentially restricted for adults only.
    '''
    class_: Literal['https://schema.org/AdultOrientedEnumeration'] = Field( # type: ignore
        default='https://schema.org/AdultOrientedEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
