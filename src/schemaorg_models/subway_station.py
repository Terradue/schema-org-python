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

class SubwayStation(CivicStructure):
    '''
    A subway station.
    '''
    class_: Literal['https://schema.org/SubwayStation'] = Field( # type: ignore
        default='https://schema.org/SubwayStation',
        alias='@type',
        serialization_alias='@type'
    )
