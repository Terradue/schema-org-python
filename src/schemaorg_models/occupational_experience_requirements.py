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
from .intangible import Intangible

class OccupationalExperienceRequirements(Intangible):
    '''
    Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    Attributes:
        monthsOfExperience: Indicates the minimal number of months of experience required for a position.
    '''
    class_: Literal['https://schema.org/OccupationalExperienceRequirements'] = Field( # type: ignore
        default='https://schema.org/OccupationalExperienceRequirements',
        alias='@type',
        serialization_alias='@type'
    )
    monthsOfExperience: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
