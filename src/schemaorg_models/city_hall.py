from __future__ import annotations

from .government_building import GovernmentBuilding    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CityHall(GovernmentBuilding):
    """
A city hall.
    """
    class_: Literal['https://schema.org/CityHall'] = Field( # type: ignore
        default='https://schema.org/CityHall',
        alias='@type',
        serialization_alias='@type'
    )
