from typing import Literal
from pydantic import Field
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates common types of measurement for wearables products.
    """
    class_: Literal['https://schema.org/WearableMeasurementTypeEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
