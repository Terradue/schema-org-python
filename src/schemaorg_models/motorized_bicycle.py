from __future__ import annotations

from .vehicle import Vehicle    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MotorizedBicycle(Vehicle):
    """
A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.
    """
    class_: Literal['https://schema.org/MotorizedBicycle'] = Field( # type: ignore
        default='https://schema.org/MotorizedBicycle',
        alias='@type',
        serialization_alias='@type'
    )
