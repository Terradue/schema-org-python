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

class LakeBodyOfWater(BodyOfWater):
    '''
    A lake (for example, Lake Pontrachain).
    '''
    class_: Literal['https://schema.org/LakeBodyOfWater'] = Field( # type: ignore
        default='https://schema.org/LakeBodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
