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

class GeoShape(StructuredValue):
    '''
    The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.

    Attributes:
        circle: A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.
        line: A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.
        address: Physical address of the item.
        postalCode: The postal code. For example, 94043.
        elevation: The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT\\_OF\\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters.
        addressCountry: The country. Recommended to be in 2-letter [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) format, for example "US". For backward compatibility, a 3-letter [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code such as "SGP" or a full country name such as "Singapore" can also be used.
        polygon: A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.
        box: A box is the area enclosed by the rectangle formed by two points. The first point is the lower corner, the second point is the upper corner. A box is expressed as two points separated by a space character.
    '''
    class_: Literal['https://schema.org/GeoShape'] = Field( # type: ignore
        default='https://schema.org/GeoShape',
        alias='@type',
        serialization_alias='@type'
    )
    circle: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'circle',
            'https://schema.org/circle'
        ),
        serialization_alias='https://schema.org/circle'
    )
    line: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'line',
            'https://schema.org/line'
        ),
        serialization_alias='https://schema.org/line'
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
    polygon: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'polygon',
            'https://schema.org/polygon'
        ),
        serialization_alias='https://schema.org/polygon'
    )
    box: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'box',
            'https://schema.org/box'
        ),
        serialization_alias='https://schema.org/box'
    )
