from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates common types of measurement for wearables products.
    """
    type_: Literal['https://schema.org/WearableMeasurementTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WearableMeasurementTypeEnumeration'),serialization_alias='class') # type: ignore
