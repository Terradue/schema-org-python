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

class BusStop(CivicStructure):
    '''
    A bus stop.
    '''
    class_: Literal['https://schema.org/BusStop'] = Field( # type: ignore
        default='https://schema.org/BusStop',
        alias='@type',
        serialization_alias='@type'
    )
