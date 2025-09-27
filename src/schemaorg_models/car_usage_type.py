from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class CarUsageType(Enumeration):
    """
A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    """
    type_: Literal['https://schema.org/CarUsageType'] = Field(default='https://schema.org/CarUsageType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
