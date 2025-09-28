from __future__ import annotations
from datetime import (
    date,
    datetime
)
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .product import Product
    from .order import Order
    from .delivery_method import DeliveryMethod
    from .postal_address import PostalAddress
    from .delivery_event import DeliveryEvent
    from .person import Person

class ParcelDelivery(Intangible):
    """
The delivery of a parcel either via the postal service or a commercial service.
    """
    class_: Literal['https://schema.org/ParcelDelivery'] = Field( # type: ignore
        default='https://schema.org/ParcelDelivery',
        alias='@type',
        serialization_alias='@type'
    )
    hasDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDeliveryMethod',
            'https://schema.org/hasDeliveryMethod'
        ),
        serialization_alias='https://schema.org/hasDeliveryMethod'
    )
    expectedArrivalUntil: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectedArrivalUntil',
            'https://schema.org/expectedArrivalUntil'
        ),
        serialization_alias='https://schema.org/expectedArrivalUntil'
    )
    originAddress: Optional[Union[PostalAddress, List[PostalAddress]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'originAddress',
            'https://schema.org/originAddress'
        ),
        serialization_alias='https://schema.org/originAddress'
    )
    deliveryAddress: Optional[Union[PostalAddress, List[PostalAddress]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryAddress',
            'https://schema.org/deliveryAddress'
        ),
        serialization_alias='https://schema.org/deliveryAddress'
    )
    itemShipped: Optional[Union[Product, List[Product]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemShipped',
            'https://schema.org/itemShipped'
        ),
        serialization_alias='https://schema.org/itemShipped'
    )
    trackingNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trackingNumber',
            'https://schema.org/trackingNumber'
        ),
        serialization_alias='https://schema.org/trackingNumber'
    )
    provider: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    trackingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trackingUrl',
            'https://schema.org/trackingUrl'
        ),
        serialization_alias='https://schema.org/trackingUrl'
    )
    expectedArrivalFrom: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectedArrivalFrom',
            'https://schema.org/expectedArrivalFrom'
        ),
        serialization_alias='https://schema.org/expectedArrivalFrom'
    )
    carrier: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'carrier',
            'https://schema.org/carrier'
        ),
        serialization_alias='https://schema.org/carrier'
    )
    deliveryStatus: Optional[Union[DeliveryEvent, List[DeliveryEvent]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryStatus',
            'https://schema.org/deliveryStatus'
        ),
        serialization_alias='https://schema.org/deliveryStatus'
    )
    partOfOrder: Optional[Union[Order, List[Order]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfOrder',
            'https://schema.org/partOfOrder'
        ),
        serialization_alias='https://schema.org/partOfOrder'
    )
