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

class Volcano(Landform):
    '''
    A volcano, like Fujisan.
    '''
    class_: Literal['https://schema.org/Volcano'] = Field( # type: ignore
        default='https://schema.org/Volcano',
        alias='@type',
        serialization_alias='@type'
    )
