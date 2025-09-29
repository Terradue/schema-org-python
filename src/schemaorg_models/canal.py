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
from .body_of_water import BodyOfWater

class Canal(BodyOfWater):
    '''
    A canal, like the Panama Canal.
    '''
    class_: Literal['https://schema.org/Canal'] = Field( # type: ignore
        default='https://schema.org/Canal',
        alias='@type',
        serialization_alias='@type'
    )
