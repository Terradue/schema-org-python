from __future__ import annotations

from .place import Place    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LandmarksOrHistoricalBuildings(Place):
    """
An historical landmark or building.
    """
    class_: Literal['https://schema.org/LandmarksOrHistoricalBuildings'] = Field( # type: ignore
        default='https://schema.org/LandmarksOrHistoricalBuildings',
        alias='@type',
        serialization_alias='@type'
    )
