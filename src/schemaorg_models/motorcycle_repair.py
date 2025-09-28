from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class MotorcycleRepair(AutomotiveBusiness):
    """
A motorcycle repair shop.
    """
    class_: Literal['https://schema.org/MotorcycleRepair'] = Field( # type: ignore
        default='https://schema.org/MotorcycleRepair',
        alias='@type',
        serialization_alias='@type'
    )
