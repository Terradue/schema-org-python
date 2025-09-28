from __future__ import annotations

from .sports_activity_location import SportsActivityLocation    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BowlingAlley(SportsActivityLocation):
    """
A bowling alley.
    """
    class_: Literal['https://schema.org/BowlingAlley'] = Field( # type: ignore
        default='https://schema.org/BowlingAlley',
        alias='@type',
        serialization_alias='@type'
    )
