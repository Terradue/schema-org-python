from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .home_and_construction_business import HomeAndConstructionBusiness

class RoofingContractor(HomeAndConstructionBusiness):
    """
A roofing contractor.
    """
    class_: Literal['https://schema.org/RoofingContractor'] = Field( # type: ignore
        default='https://schema.org/RoofingContractor',
        alias='@type',
        serialization_alias='@type'
    )
