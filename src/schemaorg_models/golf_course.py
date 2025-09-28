from __future__ import annotations

from .sports_activity_location import SportsActivityLocation    

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
