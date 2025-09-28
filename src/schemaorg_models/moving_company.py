from __future__ import annotations

from .home_and_construction_business import HomeAndConstructionBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MovingCompany(HomeAndConstructionBusiness):
    """
A moving company.
    """
    class_: Literal['https://schema.org/MovingCompany'] = Field( # type: ignore
        default='https://schema.org/MovingCompany',
        alias='@type',
        serialization_alias='@type'
    )
