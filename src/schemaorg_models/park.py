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
from .civic_structure import CivicStructure

class Park(CivicStructure):
    '''
    A park.
    '''
    class_: Literal['https://schema.org/Park'] = Field( # type: ignore
        default='https://schema.org/Park',
        alias='@type',
        serialization_alias='@type'
    )
