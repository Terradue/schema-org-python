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

class Synagogue(PlaceOfWorship):
    '''
    A synagogue.
    '''
    class_: Literal['https://schema.org/Synagogue'] = Field( # type: ignore
        default='https://schema.org/Synagogue',
        alias='@type',
        serialization_alias='@type'
    )
