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
from .price_specification import PriceSpecification
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .geo_shape import GeoShape
    from .delivery_method import DeliveryMethod
    from .place import Place
    from .administrative_area import AdministrativeArea

class DeliveryChargeSpecification(PriceSpecification):
    '''
    The price for the delivery of an offer using a particular delivery method.

    Attributes:
        areaServed: The geographic area where a service or offered item is provided.
        eligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.\
\
See also [[ineligibleRegion]].
    
        appliesToDeliveryMethod: The delivery method(s) to which the delivery charge or payment charge specification applies.
        ineligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\
\
See also [[eligibleRegion]].
      
    '''
    class_: Literal['https://schema.org/DeliveryChargeSpecification'] = Field( # type: ignore
        default='https://schema.org/DeliveryChargeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    areaServed: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'AdministrativeArea', List['AdministrativeArea'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
    eligibleRegion: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion',
            'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion'
    )
    appliesToDeliveryMethod: Optional[Union['DeliveryMethod', List['DeliveryMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToDeliveryMethod',
            'https://schema.org/appliesToDeliveryMethod'
        ),
        serialization_alias='https://schema.org/appliesToDeliveryMethod'
    )
    ineligibleRegion: Optional[Union[str, List[str], 'Place', List['Place'], 'GeoShape', List['GeoShape']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion',
            'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion'
    )
