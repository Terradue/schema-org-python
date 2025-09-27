from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.residence import Residence


class ApartmentComplex(Residence):
    """
Residence type: Apartment complex.
    """
    type_: Literal['https://schema.org/ApartmentComplex'] = Field(default='https://schema.org/ApartmentComplex', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('tourBookingPage', 'https://schema.org/tourBookingPage'), serialization_alias='https://schema.org/tourBookingPage')
    @field_serializer('tourBookingPage')
    def tourBookingPage2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    numberOfAvailableAccommodationUnits: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfAvailableAccommodationUnits', 'https://schema.org/numberOfAvailableAccommodationUnits'), serialization_alias='https://schema.org/numberOfAvailableAccommodationUnits')
    numberOfBedrooms: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfBedrooms', 'https://schema.org/numberOfBedrooms'), serialization_alias='https://schema.org/numberOfBedrooms')
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('petsAllowed', 'https://schema.org/petsAllowed'), serialization_alias='https://schema.org/petsAllowed')
    numberOfAccommodationUnits: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfAccommodationUnits', 'https://schema.org/numberOfAccommodationUnits'), serialization_alias='https://schema.org/numberOfAccommodationUnits')
