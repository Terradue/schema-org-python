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
from .price_specification import PriceSpecification
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .administrative_area import AdministrativeArea
    from .delivery_method import DeliveryMethod
    from .place import Place
    from .geo_shape import GeoShape

class DeliveryChargeSpecification(PriceSpecification):
    """
The price for the delivery of an offer using a particular delivery method.
    """
    class_: Literal['https://schema.org/DeliveryChargeSpecification'] = Field( # type: ignore
        default='https://schema.org/DeliveryChargeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    areaServed: Optional[Union[GeoShape, List[GeoShape], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape], str, List[str], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion',
            'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion'
    )
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToDeliveryMethod',
            'https://schema.org/appliesToDeliveryMethod'
        ),
        serialization_alias='https://schema.org/appliesToDeliveryMethod'
    )
    ineligibleRegion: Optional[Union[str, List[str], Place, List[Place], GeoShape, List[GeoShape]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion',
            'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion'
    )
