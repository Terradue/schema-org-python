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

class ExerciseGym(SportsActivityLocation):
    '''
    A gym.
    '''
    class_: Literal['https://schema.org/ExerciseGym'] = Field( # type: ignore
        default='https://schema.org/ExerciseGym',
        alias='@type',
        serialization_alias='@type'
    )
