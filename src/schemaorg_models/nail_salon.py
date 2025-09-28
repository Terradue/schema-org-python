from __future__ import annotations

from .health_and_beauty_business import HealthAndBeautyBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class NailSalon(HealthAndBeautyBusiness):
    """
A nail salon.
    """
    class_: Literal['https://schema.org/NailSalon'] = Field( # type: ignore
        default='https://schema.org/NailSalon',
        alias='@type',
        serialization_alias='@type'
    )
