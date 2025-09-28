from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class MeasurementMethodEnum(Enumeration):
    """
Enumeration(s) for use with [[measurementMethod]].
    """
    class_: Literal['https://schema.org/MeasurementMethodEnum'] = Field( # type: ignore
        default='https://schema.org/MeasurementMethodEnum',
        alias='@type',
        serialization_alias='@type'
    )
