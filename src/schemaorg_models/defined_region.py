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
    from .postal_code_range_specification import PostalCodeRangeSpecification

class DefinedRegion(StructuredValue):
    '''
    A DefinedRegion is a geographic area defined by potentially arbitrary (rather than political, administrative or natural geographical) criteria. Properties are provided for defining a region by reference to sets of postal codes.

Examples: a delivery destination when shopping. Region where regional pricing is configured.

Requirement 1:
Country: US
States: "NY", "CA"

Requirement 2:
Country: US
PostalCode Set: { [94000-94585], [97000, 97999], [13000, 13599]}
{ [12345, 12345], [78945, 78945], }
Region = state, canton, prefecture, autonomous community...


    Attributes:
        postalCodeRange: A defined range of postal codes.
        addressRegion: The region in which the locality is, and which is in the country. For example, California or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country).
        postalCode: The postal code. For example, 94043.
        addressCountry: The country. Recommended to be in 2-letter [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) format, for example "US". For backward compatibility, a 3-letter [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code such as "SGP" or a full country name such as "Singapore" can also be used.
        postalCodePrefix: A defined range of postal codes indicated by a common textual prefix. Used for non-numeric systems such as UK.
    '''
    class_: Literal['https://schema.org/DefinedRegion'] = Field( # type: ignore
        default='https://schema.org/DefinedRegion',
        alias='@type',
        serialization_alias='@type'
    )
    postalCodeRange: Optional[Union['PostalCodeRangeSpecification', List['PostalCodeRangeSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodeRange',
            'https://schema.org/postalCodeRange'
        ),
        serialization_alias='https://schema.org/postalCodeRange'
    )
    addressRegion: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressRegion',
            'https://schema.org/addressRegion'
        ),
        serialization_alias='https://schema.org/addressRegion'
    )
    postalCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCode',
            'https://schema.org/postalCode'
        ),
        serialization_alias='https://schema.org/postalCode'
    )
    addressCountry: Optional[Union[str, List[str], 'Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry',
            'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry'
    )
    postalCodePrefix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodePrefix',
            'https://schema.org/postalCodePrefix'
        ),
        serialization_alias='https://schema.org/postalCodePrefix'
    )
