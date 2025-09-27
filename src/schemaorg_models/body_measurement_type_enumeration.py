from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.
    """
    type_: Literal['https://schema.org/BodyMeasurementTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BodyMeasurementTypeEnumeration'),serialization_alias='class') # type: ignore
