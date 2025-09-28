from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .health_and_beauty_business import HealthAndBeautyBusiness

class BeautySalon(HealthAndBeautyBusiness):
    """
Beauty salon.
    """
    class_: Literal['https://schema.org/BeautySalon'] = Field( # type: ignore
        default='https://schema.org/BeautySalon',
        alias='@type',
        serialization_alias='@type'
    )
