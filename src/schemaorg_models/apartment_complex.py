from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.residence import Residence


class ApartmentComplex(Residence):
    """
Residence type: Apartment complex.
    """
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('tourBookingPage', 'https://schema.org/tourBookingPage'),serialization_alias='https://schema.org/tourBookingPage')
    numberOfAvailableAccommodationUnits: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfAvailableAccommodationUnits', 'https://schema.org/numberOfAvailableAccommodationUnits'),serialization_alias='https://schema.org/numberOfAvailableAccommodationUnits')
    numberOfBedrooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfBedrooms', 'https://schema.org/numberOfBedrooms'),serialization_alias='https://schema.org/numberOfBedrooms')
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('petsAllowed', 'https://schema.org/petsAllowed'),serialization_alias='https://schema.org/petsAllowed')
    numberOfAccommodationUnits: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfAccommodationUnits', 'https://schema.org/numberOfAccommodationUnits'),serialization_alias='https://schema.org/numberOfAccommodationUnits')
