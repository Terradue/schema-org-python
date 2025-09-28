from __future__ import annotations

from .qualitative_value import QualitativeValue    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SteeringPositionValue(QualitativeValue):
    """
A value indicating a steering position.
    """
    class_: Literal['https://schema.org/SteeringPositionValue'] = Field( # type: ignore
        default='https://schema.org/SteeringPositionValue',
        alias='@type',
        serialization_alias='@type'
    )
