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

class DanceEvent(Event):
    '''
    Event type: A social dance.
    '''
    class_: Literal['https://schema.org/DanceEvent'] = Field( # type: ignore
        default='https://schema.org/DanceEvent',
        alias='@type',
        serialization_alias='@type'
    )
