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

class Continent(Landform):
    '''
    One of the continents (for example, Europe or Africa).
    '''
    class_: Literal['https://schema.org/Continent'] = Field( # type: ignore
        default='https://schema.org/Continent',
        alias='@type',
        serialization_alias='@type'
    )
