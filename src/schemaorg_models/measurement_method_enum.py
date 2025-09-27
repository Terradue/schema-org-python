from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MeasurementMethodEnum(Enumeration):
    """
Enumeration(s) for use with [[measurementMethod]].
    """
    class_: Literal['https://schema.org/MeasurementMethodEnum'] = Field(default='https://schema.org/MeasurementMethodEnum', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
