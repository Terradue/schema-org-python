from __future__ import annotations

from .home_and_construction_business import HomeAndConstructionBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HousePainter(HomeAndConstructionBusiness):
    """
A house painting service.
    """
    class_: Literal['https://schema.org/HousePainter'] = Field( # type: ignore
        default='https://schema.org/HousePainter',
        alias='@type',
        serialization_alias='@type'
    )
