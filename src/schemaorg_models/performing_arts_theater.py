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

class PerformingArtsTheater(CivicStructure):
    '''
    A theater or other performing art center.
    '''
    class_: Literal['https://schema.org/PerformingArtsTheater'] = Field( # type: ignore
        default='https://schema.org/PerformingArtsTheater',
        alias='@type',
        serialization_alias='@type'
    )
