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
from .sports_activity_location import SportsActivityLocation

class TennisComplex(SportsActivityLocation):
    '''
    A tennis complex.
    '''
    class_: Literal['https://schema.org/TennisComplex'] = Field( # type: ignore
        default='https://schema.org/TennisComplex',
        alias='@type',
        serialization_alias='@type'
    )
