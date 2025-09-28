from __future__ import annotations

from .entertainment_business import EntertainmentBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AdultEntertainment(EntertainmentBusiness):
    """
An adult entertainment establishment.
    """
    class_: Literal['https://schema.org/AdultEntertainment'] = Field( # type: ignore
        default='https://schema.org/AdultEntertainment',
        alias='@type',
        serialization_alias='@type'
    )
