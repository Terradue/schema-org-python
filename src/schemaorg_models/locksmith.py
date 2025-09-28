from __future__ import annotations

from .home_and_construction_business import HomeAndConstructionBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Locksmith(HomeAndConstructionBusiness):
    """
A locksmith.
    """
    class_: Literal['https://schema.org/Locksmith'] = Field( # type: ignore
        default='https://schema.org/Locksmith',
        alias='@type',
        serialization_alias='@type'
    )
