from typing import Literal
from pydantic import Field
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.
    """
    class_: Literal['https://schema.org/BodyMeasurementTypeEnumeration'] = Field(default='https://schema.org/BodyMeasurementTypeEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
