from __future__ import annotations

from .automotive_business import AutomotiveBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutoRental(AutomotiveBusiness):
    """
A car rental business.
    """
    class_: Literal['https://schema.org/AutoRental'] = Field( # type: ignore
        default='https://schema.org/AutoRental',
        alias='@type',
        serialization_alias='@type'
    )
