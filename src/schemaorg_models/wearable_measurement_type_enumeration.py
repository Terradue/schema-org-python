from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .measurement_type_enumeration import MeasurementTypeEnumeration

class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates common types of measurement for wearables products.
    """
    class_: Literal['https://schema.org/WearableMeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableMeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
