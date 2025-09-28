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

class GolfCourse(SportsActivityLocation):
    """
A golf course.
    """
    class_: Literal['https://schema.org/GolfCourse'] = Field( # type: ignore
        default='https://schema.org/GolfCourse',
        alias='@type',
        serialization_alias='@type'
    )
