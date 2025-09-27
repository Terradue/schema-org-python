from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """
Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.
    """
    class_: Literal['https://schema.org/MeasurementTypeEnumeration'] = Field(default='https://schema.org/MeasurementTypeEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
