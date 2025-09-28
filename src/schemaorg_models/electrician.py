from __future__ import annotations

from .home_and_construction_business import HomeAndConstructionBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Electrician(HomeAndConstructionBusiness):
    """
An electrician.
    """
    class_: Literal['https://schema.org/Electrician'] = Field( # type: ignore
        default='https://schema.org/Electrician',
        alias='@type',
        serialization_alias='@type'
    )
