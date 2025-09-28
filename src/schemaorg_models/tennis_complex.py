from __future__ import annotations

from .sports_activity_location import SportsActivityLocation    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TennisComplex(SportsActivityLocation):
    """
A tennis complex.
    """
    class_: Literal['https://schema.org/TennisComplex'] = Field( # type: ignore
        default='https://schema.org/TennisComplex',
        alias='@type',
        serialization_alias='@type'
    )
