from typing import Literal
from pydantic import Field
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.
    """
    class_: Literal['https://schema.org/BodyMeasurementTypeEnumeration'] = Field(default='https://schema.org/BodyMeasurementTypeEnumeration', alias='@type', serialization_alias='@type') # type: ignore
