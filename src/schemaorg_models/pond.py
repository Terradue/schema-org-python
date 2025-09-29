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

class Pond(BodyOfWater):
    '''
    A pond.
    '''
    class_: Literal['https://schema.org/Pond'] = Field( # type: ignore
        default='https://schema.org/Pond',
        alias='@type',
        serialization_alias='@type'
    )
