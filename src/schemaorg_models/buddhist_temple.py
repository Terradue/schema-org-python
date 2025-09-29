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
from .place_of_worship import PlaceOfWorship

class BuddhistTemple(PlaceOfWorship):
    '''
    A Buddhist temple.
    '''
    class_: Literal['https://schema.org/BuddhistTemple'] = Field( # type: ignore
        default='https://schema.org/BuddhistTemple',
        alias='@type',
        serialization_alias='@type'
    )
