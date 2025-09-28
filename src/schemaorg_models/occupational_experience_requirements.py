from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

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
