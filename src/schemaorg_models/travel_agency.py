from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class TravelAgency(LocalBusiness):
    """
A travel agency.
    """
    class_: Literal['https://schema.org/TravelAgency'] = Field( # type: ignore
        default='https://schema.org/TravelAgency',
        alias='@type',
        serialization_alias='@type'
    )
