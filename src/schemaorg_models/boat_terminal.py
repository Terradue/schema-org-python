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

class BoatTerminal(CivicStructure):
    '''
    A terminal for boats, ships, and other water vessels.
    '''
    class_: Literal['https://schema.org/BoatTerminal'] = Field( # type: ignore
        default='https://schema.org/BoatTerminal',
        alias='@type',
        serialization_alias='@type'
    )
