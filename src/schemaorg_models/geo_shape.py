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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .postal_address import PostalAddress
    from .country import Country

class GeoShape(StructuredValue):
    """
The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.
    """
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
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = Field(
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
    addressCountry: Optional[Union[str, List[str], "Country", List["Country"]]] = Field(
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
