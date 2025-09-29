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

class SeaBodyOfWater(BodyOfWater):
    '''
    A sea (for example, the Caspian sea).
    '''
    class_: Literal['https://schema.org/SeaBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/SeaBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
