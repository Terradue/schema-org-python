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

class GameAvailabilityEnumeration(Enumeration):
    '''
    For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 
    '''
    class_: Literal['https://schema.org/GameAvailabilityEnumeration'] = Field( # type: ignore
        default='https://schema.org/GameAvailabilityEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
