from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .entertainment_business import EntertainmentBusiness

class Casino(EntertainmentBusiness):
    """
A casino.
    """
    class_: Literal['https://schema.org/Casino'] = Field( # type: ignore
        default='https://schema.org/Casino',
        alias='@type',
        serialization_alias='@type'
    )
