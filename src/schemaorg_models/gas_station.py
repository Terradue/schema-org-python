from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class GasStation(AutomotiveBusiness):
    """
A gas station.
    """
    class_: Literal['https://schema.org/GasStation'] = Field( # type: ignore
        default='https://schema.org/GasStation',
        alias='@type',
        serialization_alias='@type'
    )
