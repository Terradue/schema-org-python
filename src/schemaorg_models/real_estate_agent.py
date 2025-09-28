from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RealEstateAgent(LocalBusiness):
    """
A real-estate agent.
    """
    class_: Literal['https://schema.org/RealEstateAgent'] = Field( # type: ignore
        default='https://schema.org/RealEstateAgent',
        alias='@type',
        serialization_alias='@type'
    )
