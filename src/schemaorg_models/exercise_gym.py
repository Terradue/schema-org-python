from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.sports_activity_location import SportsActivityLocation

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ExerciseGym(SportsActivityLocation):
    """
A gym.
    """
    class_: Literal['https://schema.org/ExerciseGym'] = Field( # type: ignore
        default='https://schema.org/ExerciseGym',
        alias='@type',
        serialization_alias='@type'
    )
