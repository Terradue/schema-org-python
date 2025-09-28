from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .health_and_beauty_business import HealthAndBeautyBusiness

class HairSalon(HealthAndBeautyBusiness):
    """
A hair salon.
    """
    class_: Literal['https://schema.org/HairSalon'] = Field( # type: ignore
        default='https://schema.org/HairSalon',
        alias='@type',
        serialization_alias='@type'
    )
