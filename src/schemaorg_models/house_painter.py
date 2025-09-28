from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .home_and_construction_business import HomeAndConstructionBusiness

class HousePainter(HomeAndConstructionBusiness):
    """
A house painting service.
    """
    class_: Literal['https://schema.org/HousePainter'] = Field( # type: ignore
        default='https://schema.org/HousePainter',
        alias='@type',
        serialization_alias='@type'
    )
