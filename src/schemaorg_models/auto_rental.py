from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class AutoRental(AutomotiveBusiness):
    """
A car rental business.
    """
    class_: Literal['https://schema.org/AutoRental'] = Field( # type: ignore
        default='https://schema.org/AutoRental',
        alias='@type',
        serialization_alias='@type'
    )
