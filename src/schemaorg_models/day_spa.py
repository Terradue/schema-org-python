from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .health_and_beauty_business import HealthAndBeautyBusiness

class DaySpa(HealthAndBeautyBusiness):
    """
A day spa.
    """
    class_: Literal['https://schema.org/DaySpa'] = Field( # type: ignore
        default='https://schema.org/DaySpa',
        alias='@type',
        serialization_alias='@type'
    )
