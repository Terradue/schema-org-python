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
from .enumeration import Enumeration

class RsvpResponseType(Enumeration):
    '''
    RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    '''
    class_: Literal['https://schema.org/RsvpResponseType'] = Field( # type: ignore
        default='https://schema.org/RsvpResponseType',
        alias='@type',
        serialization_alias='@type'
    )
