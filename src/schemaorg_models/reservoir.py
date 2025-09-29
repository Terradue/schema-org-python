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

class Reservoir(BodyOfWater):
    '''
    A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.
    '''
    class_: Literal['https://schema.org/Reservoir'] = Field( # type: ignore
        default='https://schema.org/Reservoir',
        alias='@type',
        serialization_alias='@type'
    )
