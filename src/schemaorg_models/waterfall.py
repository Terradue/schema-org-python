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

class Waterfall(BodyOfWater):
    '''
    A waterfall, like Niagara.
    '''
    class_: Literal['https://schema.org/Waterfall'] = Field( # type: ignore
        default='https://schema.org/Waterfall',
        alias='@type',
        serialization_alias='@type'
    )
