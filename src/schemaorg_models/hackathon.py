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

class Hackathon(Event):
    '''
    A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    '''
    class_: Literal['https://schema.org/Hackathon'] = Field( # type: ignore
        default='https://schema.org/Hackathon',
        alias='@type',
        serialization_alias='@type'
    )
