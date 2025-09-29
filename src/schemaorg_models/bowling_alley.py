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

class BowlingAlley(SportsActivityLocation):
    '''
    A bowling alley.
    '''
    class_: Literal['https://schema.org/BowlingAlley'] = Field( # type: ignore
        default='https://schema.org/BowlingAlley',
        alias='@type',
        serialization_alias='@type'
    )
