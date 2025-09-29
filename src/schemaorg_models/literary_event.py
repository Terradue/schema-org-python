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

class LiteraryEvent(Event):
    '''
    Event type: Literary event.
    '''
    class_: Literal['https://schema.org/LiteraryEvent'] = Field( # type: ignore
        default='https://schema.org/LiteraryEvent',
        alias='@type',
        serialization_alias='@type'
    )
