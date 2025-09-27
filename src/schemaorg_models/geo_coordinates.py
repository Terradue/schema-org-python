from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.country import Country

class GeoCoordinates(StructuredValue):
    """
The geographic coordinates of a place or event.
    """
    class_: Literal['https://schema.org/GeoCoordinates'] = Field(default='https://schema.org/GeoCoordinates', alias='@type', serialization_alias='@type') # type: ignore
    longitude: Optional[Union[float, List[float], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('longitude', 'https://schema.org/longitude'), serialization_alias='https://schema.org/longitude')
    latitude: Optional[Union[str, List[str], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('latitude', 'https://schema.org/latitude'), serialization_alias='https://schema.org/latitude')
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = Field(default=None, validation_alias=AliasChoices('address', 'https://schema.org/address'), serialization_alias='https://schema.org/address')
    postalCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'), serialization_alias='https://schema.org/postalCode')
    elevation: Optional[Union[str, List[str], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('elevation', 'https://schema.org/elevation'), serialization_alias='https://schema.org/elevation')
    addressCountry: Optional[Union[str, List[str], Country, List[Country]]] = Field(default=None, validation_alias=AliasChoices('addressCountry', 'https://schema.org/addressCountry'), serialization_alias='https://schema.org/addressCountry')
