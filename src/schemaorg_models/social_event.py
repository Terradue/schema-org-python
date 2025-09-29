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

class SocialEvent(Event):
    '''
    Event type: Social event.
    '''
    class_: Literal['https://schema.org/SocialEvent'] = Field( # type: ignore
        default='https://schema.org/SocialEvent',
        alias='@type',
        serialization_alias='@type'
    )
