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

class GolfCourse(SportsActivityLocation):
    '''
    A golf course.
    '''
    class_: Literal['https://schema.org/GolfCourse'] = Field( # type: ignore
        default='https://schema.org/GolfCourse',
        alias='@type',
        serialization_alias='@type'
    )
