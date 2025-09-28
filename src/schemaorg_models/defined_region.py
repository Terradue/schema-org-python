from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .postal_code_range_specification import PostalCodeRangeSpecification
from .structured_value import StructuredValue
from .country import Country

class DefinedRegion(StructuredValue):
    """
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

    """
    class_: Literal['https://schema.org/DefinedRegion'] = Field( # type: ignore
        default='https://schema.org/DefinedRegion',
        alias='@type',
        serialization_alias='@type'
    )
    postalCodeRange: Optional[Union[PostalCodeRangeSpecification, List[PostalCodeRangeSpecification]]] = Field(
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
    addressCountry: Optional[Union[str, List[str], Country, List[Country]]] = Field(
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
