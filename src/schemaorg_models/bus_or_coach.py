from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.vehicle import Vehicle

from schemaorg_models.quantitative_value import QuantitativeValue

class BusOrCoach(Vehicle):
    """
A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches are luxury buses, usually in service for long distance travel.
    """
    type_: Literal['https://schema.org/BusOrCoach'] = Field(default='https://schema.org/BusOrCoach', alias='@type', serialization_alias='@type') # type: ignore
    roofLoad: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('roofLoad', 'https://schema.org/roofLoad'), serialization_alias='https://schema.org/roofLoad')
    acrissCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('acrissCode', 'https://schema.org/acrissCode'), serialization_alias='https://schema.org/acrissCode')
