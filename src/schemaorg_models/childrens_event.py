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

class ChildrensEvent(Event):
    '''
    Event type: Children's event.
    '''
    class_: Literal['https://schema.org/ChildrensEvent'] = Field( # type: ignore
        default='https://schema.org/ChildrensEvent',
        alias='@type',
        serialization_alias='@type'
    )
