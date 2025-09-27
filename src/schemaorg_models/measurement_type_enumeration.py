from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """
Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.
    """
    type_: Literal['https://schema.org/MeasurementTypeEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MeasurementTypeEnumeration'),serialization_alias='class') # type: ignore
