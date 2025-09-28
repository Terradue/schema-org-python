from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .entertainment_business import EntertainmentBusiness

class AdultEntertainment(EntertainmentBusiness):
    """
An adult entertainment establishment.
    """
    class_: Literal['https://schema.org/AdultEntertainment'] = Field( # type: ignore
        default='https://schema.org/AdultEntertainment',
        alias='@type',
        serialization_alias='@type'
    )
