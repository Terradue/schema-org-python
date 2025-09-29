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

class Playground(CivicStructure):
    '''
    A playground.
    '''
    class_: Literal['https://schema.org/Playground'] = Field( # type: ignore
        default='https://schema.org/Playground',
        alias='@type',
        serialization_alias='@type'
    )
