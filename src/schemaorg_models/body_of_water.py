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
from .landform import Landform

class BodyOfWater(Landform):
    '''
    A body of water, such as a sea, ocean, or lake.
    '''
    class_: Literal['https://schema.org/BodyOfWater'] = Field( # type: ignore
        default='https://schema.org/BodyOfWater',
        alias='@type',
        serialization_alias='@type'
    )
