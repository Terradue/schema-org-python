from __future__ import annotations

from .home_and_construction_business import HomeAndConstructionBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Plumber(HomeAndConstructionBusiness):
    """
A plumbing service.
    """
    class_: Literal['https://schema.org/Plumber'] = Field( # type: ignore
        default='https://schema.org/Plumber',
        alias='@type',
        serialization_alias='@type'
    )
