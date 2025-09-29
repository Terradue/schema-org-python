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

class Museum(CivicStructure):
    '''
    A museum.
    '''
    class_: Literal['https://schema.org/Museum'] = Field( # type: ignore
        default='https://schema.org/Museum',
        alias='@type',
        serialization_alias='@type'
    )
