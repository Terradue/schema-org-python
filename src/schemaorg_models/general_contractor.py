from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .home_and_construction_business import HomeAndConstructionBusiness

class GeneralContractor(HomeAndConstructionBusiness):
    """
A general contractor.
    """
    class_: Literal['https://schema.org/GeneralContractor'] = Field( # type: ignore
        default='https://schema.org/GeneralContractor',
        alias='@type',
        serialization_alias='@type'
    )
