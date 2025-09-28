from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class MotorcycleDealer(AutomotiveBusiness):
    """
A motorcycle dealer.
    """
    class_: Literal['https://schema.org/MotorcycleDealer'] = Field( # type: ignore
        default='https://schema.org/MotorcycleDealer',
        alias='@type',
        serialization_alias='@type'
    )
