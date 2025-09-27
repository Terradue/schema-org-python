from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.country import Country

class GeoShape(StructuredValue):
    """
The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.
    """
    class_: Literal['https://schema.org/GeoShape'] = Field(default='https://schema.org/GeoShape', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    circle: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('circle', 'https://schema.org/circle'), serialization_alias='https://schema.org/circle')
    line: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('line', 'https://schema.org/line'), serialization_alias='https://schema.org/line')
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = Field(default=None, validation_alias=AliasChoices('address', 'https://schema.org/address'), serialization_alias='https://schema.org/address')
    postalCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'), serialization_alias='https://schema.org/postalCode')
    elevation: Optional[Union[str, List[str], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('elevation', 'https://schema.org/elevation'), serialization_alias='https://schema.org/elevation')
    addressCountry: Optional[Union[str, List[str], Country, List[Country]]] = Field(default=None, validation_alias=AliasChoices('addressCountry', 'https://schema.org/addressCountry'), serialization_alias='https://schema.org/addressCountry')
    polygon: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('polygon', 'https://schema.org/polygon'), serialization_alias='https://schema.org/polygon')
    box: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('box', 'https://schema.org/box'), serialization_alias='https://schema.org/box')
