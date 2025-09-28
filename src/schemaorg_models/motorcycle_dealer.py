from __future__ import annotations

from .automotive_business import AutomotiveBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MotorcycleDealer(AutomotiveBusiness):
    """
A motorcycle dealer.
    """
    class_: Literal['https://schema.org/MotorcycleDealer'] = Field( # type: ignore
        default='https://schema.org/MotorcycleDealer',
        alias='@type',
        serialization_alias='@type'
    )
