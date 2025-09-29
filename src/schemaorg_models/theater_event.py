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
from .event import Event

class TheaterEvent(Event):
    '''
    Event type: Theater performance.
    '''
    class_: Literal['https://schema.org/TheaterEvent'] = Field( # type: ignore
        default='https://schema.org/TheaterEvent',
        alias='@type',
        serialization_alias='@type'
    )
