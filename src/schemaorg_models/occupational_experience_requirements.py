from __future__ import annotations

from .intangible import Intangible    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class OccupationalExperienceRequirements(Intangible):
    """
Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].
    """
    class_: Literal['https://schema.org/OccupationalExperienceRequirements'] = Field( # type: ignore
        default='https://schema.org/OccupationalExperienceRequirements',
        alias='@type',
        serialization_alias='@type'
    )
    monthsOfExperience: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'monthsOfExperience',
            'https://schema.org/monthsOfExperience'
        ),
        serialization_alias='https://schema.org/monthsOfExperience'
    )
