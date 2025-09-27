from typing import Literal
from pydantic import Field
from schemaorg_models.measurement_type_enumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
Enumerates common types of measurement for wearables products.
    """
    class_: Literal['https://schema.org/WearableMeasurementTypeEnumeration'] = Field(default='https://schema.org/WearableMeasurementTypeEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
