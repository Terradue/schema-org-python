from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .sports_activity_location import SportsActivityLocation

class TennisComplex(SportsActivityLocation):
    """
A tennis complex.
    """
    class_: Literal['https://schema.org/TennisComplex'] = Field( # type: ignore
        default='https://schema.org/TennisComplex',
        alias='@type',
        serialization_alias='@type'
    )
