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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .product import Product
    from .delivery_method import DeliveryMethod
    from .person import Person
    from .delivery_event import DeliveryEvent
    from .organization import Organization
    from .order import Order
    from .postal_address import PostalAddress

class ParcelDelivery(Intangible):
    '''
    The delivery of a parcel either via the postal service or a commercial service.

    Attributes:
        hasDeliveryMethod: Method used for delivery or shipping.
        expectedArrivalUntil: The latest date the package may arrive.
        originAddress: Shipper's address.
        deliveryAddress: Destination address.
        itemShipped: Item(s) being shipped.
        trackingNumber: Shipper tracking number.
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        trackingUrl: Tracking url for the parcel delivery.
        expectedArrivalFrom: The earliest date the package may arrive.
        carrier: 'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.
        deliveryStatus: New entry added as the package passes through each leg of its journey (from shipment to final delivery).
        partOfOrder: The overall order the items in this delivery were included in.
    '''
    class_: Literal['https://schema.org/ParcelDelivery'] = Field( # type: ignore
        default='https://schema.org/ParcelDelivery',
        alias='@type',
        serialization_alias='@type'
    )
    hasDeliveryMethod: Optional[Union['DeliveryMethod', List['DeliveryMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expectedArrivalUntil: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    originAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    deliveryAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itemShipped: Optional[Union['Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    trackingNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    trackingUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expectedArrivalFrom: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    carrier: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    deliveryStatus: Optional[Union['DeliveryEvent', List['DeliveryEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    partOfOrder: Optional[Union['Order', List['Order']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
