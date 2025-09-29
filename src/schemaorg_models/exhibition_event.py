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

class ExhibitionEvent(Event):
    '''
    Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...
    '''
    class_: Literal['https://schema.org/ExhibitionEvent'] = Field( # type: ignore
        default='https://schema.org/ExhibitionEvent',
        alias='@type',
        serialization_alias='@type'
    )
