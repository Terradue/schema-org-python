from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .country import Country
    from .postal_address import PostalAddress

class GeoCoordinates(StructuredValue):
    '''
    The geographic coordinates of a place or event.

    Attributes:
        longitude: The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        latitude: The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        address: Physical address of the item.
        postalCode: The postal code. For example, 94043.
        elevation: The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT\\_OF\\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters.
        addressCountry: The country. Recommended to be in 2-letter [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) format, for example "US". For backward compatibility, a 3-letter [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code such as "SGP" or a full country name such as "Singapore" can also be used.
    '''
    class_: Literal['https://schema.org/GeoCoordinates'] = Field( # type: ignore
        default='https://schema.org/GeoCoordinates',
        alias='@type',
        serialization_alias='@type'
    )
    longitude: Optional[Union[float, List[float], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'longitude',
            'https://schema.org/longitude'
        ),
        serialization_alias='https://schema.org/longitude'
    )
    latitude: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'latitude',
            'https://schema.org/latitude'
        ),
        serialization_alias='https://schema.org/latitude'
    )
    address: Optional[Union[str, List[str], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'address',
            'https://schema.org/address'
        ),
        serialization_alias='https://schema.org/address'
    )
    postalCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCode',
            'https://schema.org/postalCode'
        ),
        serialization_alias='https://schema.org/postalCode'
    )
    elevation: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'elevation',
            'https://schema.org/elevation'
        ),
        serialization_alias='https://schema.org/elevation'
    )
    addressCountry: Optional[Union[str, List[str], 'Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry',
            'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry'
    )
