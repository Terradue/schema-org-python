from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.vehicle import Vehicle

from schemaorg_models.quantitative_value import QuantitativeValue

class Car(Vehicle):
    """
A car is a wheeled, self-powered motor vehicle used for transportation.
    """
    class_: Literal['https://schema.org/Car'] = Field(default='https://schema.org/Car', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    roofLoad: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('roofLoad', 'https://schema.org/roofLoad'), serialization_alias='https://schema.org/roofLoad')
    acrissCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('acrissCode', 'https://schema.org/acrissCode'), serialization_alias='https://schema.org/acrissCode')
