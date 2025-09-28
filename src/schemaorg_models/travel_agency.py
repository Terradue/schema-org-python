from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TravelAgency(LocalBusiness):
    """
A travel agency.
    """
    class_: Literal['https://schema.org/TravelAgency'] = Field( # type: ignore
        default='https://schema.org/TravelAgency',
        alias='@type',
        serialization_alias='@type'
    )
