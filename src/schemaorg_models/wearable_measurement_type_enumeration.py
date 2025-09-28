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

class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates common types of measurement for wearables products.
    """
    class_: Literal['https://schema.org/WearableMeasurementTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableMeasurementTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
