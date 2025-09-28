from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .health_and_beauty_business import HealthAndBeautyBusiness

class NailSalon(HealthAndBeautyBusiness):
    """
A nail salon.
    """
    class_: Literal['https://schema.org/NailSalon'] = Field( # type: ignore
        default='https://schema.org/NailSalon',
        alias='@type',
        serialization_alias='@type'
    )
