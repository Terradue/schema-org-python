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
from .civic_structure import CivicStructure

class EventVenue(CivicStructure):
    '''
    An event venue.
    '''
    class_: Literal['https://schema.org/EventVenue'] = Field( # type: ignore
        default='https://schema.org/EventVenue',
        alias='@type',
        serialization_alias='@type'
    )
