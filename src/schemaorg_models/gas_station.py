from __future__ import annotations

from .automotive_business import AutomotiveBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GasStation(AutomotiveBusiness):
    """
A gas station.
    """
    class_: Literal['https://schema.org/GasStation'] = Field( # type: ignore
        default='https://schema.org/GasStation',
        alias='@type',
        serialization_alias='@type'
    )
