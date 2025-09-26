from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Airline(Organization):
    """
An organization that provides flights for passengers.
    """
    iataCode: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('iataCode', 'https://schema.org/iataCode'),serialization_alias='https://schema.org/iataCode')
    boardingPolicy: Optional[Union["BoardingPolicyType", List["BoardingPolicyType"]]] = Field(default=None,validation_alias=AliasChoices('boardingPolicy', 'https://schema.org/boardingPolicy'),serialization_alias='https://schema.org/boardingPolicy')
