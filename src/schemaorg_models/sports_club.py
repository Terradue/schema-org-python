from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .sports_activity_location import SportsActivityLocation

class SportsClub(SportsActivityLocation):
    """
A sports club.
    """
    class_: Literal['https://schema.org/SportsClub'] = Field( # type: ignore
        default='https://schema.org/SportsClub',
        alias='@type',
        serialization_alias='@type'
    )
