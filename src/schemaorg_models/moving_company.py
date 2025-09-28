from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .home_and_construction_business import HomeAndConstructionBusiness

class MovingCompany(HomeAndConstructionBusiness):
    """
A moving company.
    """
    class_: Literal['https://schema.org/MovingCompany'] = Field( # type: ignore
        default='https://schema.org/MovingCompany',
        alias='@type',
        serialization_alias='@type'
    )
