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
from .contact_point import ContactPoint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .country import Country

class PostalAddress(ContactPoint):
    '''
    The mailing address.

    Attributes:
        addressRegion: The region in which the locality is, and which is in the country. For example, California or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country).
        postalCode: The postal code. For example, 94043.
        streetAddress: The street address. For example, 1600 Amphitheatre Pkwy.
        addressCountry: The country. Recommended to be in 2-letter [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) format, for example "US". For backward compatibility, a 3-letter [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country code such as "SGP" or a full country name such as "Singapore" can also be used.
        addressLocality: The locality in which the street address is, and which is in the region. For example, Mountain View.
        extendedAddress: An address extension such as an apartment number, C/O or alternative name.
        postOfficeBoxNumber: The post office box number for PO box addresses.
    '''
    class_: Literal['https://schema.org/PostalAddress'] = Field( # type: ignore
        default='https://schema.org/PostalAddress',
        alias='@type',
        serialization_alias='@type'
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
    streetAddress: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'streetAddress',
            'https://schema.org/streetAddress'
        ),
        serialization_alias='https://schema.org/streetAddress'
    )
    addressCountry: Optional[Union[str, List[str], 'Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry',
            'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry'
    )
    addressLocality: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressLocality',
            'https://schema.org/addressLocality'
        ),
        serialization_alias='https://schema.org/addressLocality'
    )
    extendedAddress: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'extendedAddress',
            'https://schema.org/extendedAddress'
        ),
        serialization_alias='https://schema.org/extendedAddress'
    )
    postOfficeBoxNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postOfficeBoxNumber',
            'https://schema.org/postOfficeBoxNumber'
        ),
        serialization_alias='https://schema.org/postOfficeBoxNumber'
    )
