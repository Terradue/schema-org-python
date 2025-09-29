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

class PlaceOfWorship(CivicStructure):
    '''
    Place of worship, such as a church, synagogue, or mosque.
    '''
    class_: Literal['https://schema.org/PlaceOfWorship'] = Field( # type: ignore
        default='https://schema.org/PlaceOfWorship',
        alias='@type',
        serialization_alias='@type'
    )
