from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class RealEstateAgent(LocalBusiness):
    """
A real-estate agent.
    """
    class_: Literal['https://schema.org/RealEstateAgent'] = Field( # type: ignore
        default='https://schema.org/RealEstateAgent',
        alias='@type',
        serialization_alias='@type'
    )
