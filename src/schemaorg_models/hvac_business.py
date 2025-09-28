from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .home_and_construction_business import HomeAndConstructionBusiness

class HVACBusiness(HomeAndConstructionBusiness):
    """
A business that provides Heating, Ventilation and Air Conditioning services.
    """
    class_: Literal['https://schema.org/HVACBusiness'] = Field( # type: ignore
        default='https://schema.org/HVACBusiness',
        alias='@type',
        serialization_alias='@type'
    )
