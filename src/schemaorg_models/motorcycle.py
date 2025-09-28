from __future__ import annotations

from .vehicle import Vehicle    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Motorcycle(Vehicle):
    """
A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.
    """
    class_: Literal['https://schema.org/Motorcycle'] = Field( # type: ignore
        default='https://schema.org/Motorcycle',
        alias='@type',
        serialization_alias='@type'
    )
