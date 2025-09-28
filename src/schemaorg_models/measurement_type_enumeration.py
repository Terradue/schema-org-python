from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class MeasurementTypeEnumeration(Enumeration):
    """
Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.
    """
    class_: Literal['https://schema.org/MeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/MeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
