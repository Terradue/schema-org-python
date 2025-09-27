from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Airline(Organization):
    """
An organization that provides flights for passengers.
    """
    type_: Literal['https://schema.org/Airline'] = Field(default='https://schema.org/Airline', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    iataCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('iataCode', 'https://schema.org/iataCode'), serialization_alias='https://schema.org/iataCode')
    boardingPolicy: Optional[Union["BoardingPolicyType", List["BoardingPolicyType"]]] = Field(default=None, validation_alias=AliasChoices('boardingPolicy', 'https://schema.org/boardingPolicy'), serialization_alias='https://schema.org/boardingPolicy')
