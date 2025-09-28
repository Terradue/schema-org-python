from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.
    """
    class_: Literal['https://schema.org/BodyMeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/BodyMeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
