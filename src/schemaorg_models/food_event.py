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

class FoodEvent(Event):
    '''
    Event type: Food event.
    '''
    class_: Literal['https://schema.org/FoodEvent'] = Field( # type: ignore
        default='https://schema.org/FoodEvent',
        alias='@type',
        serialization_alias='@type'
    )
