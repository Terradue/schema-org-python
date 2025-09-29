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
    from .delivery_method import DeliveryMethod
    from .product import Product
    from .postal_address import PostalAddress
    from .organization import Organization
    from .order import Order
    from .person import Person
    from .delivery_event import DeliveryEvent

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
    originAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'originAddress',
            'https://schema.org/originAddress'
        ),
        serialization_alias='https://schema.org/originAddress'
    )
    deliveryAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryAddress',
            'https://schema.org/deliveryAddress'
        ),
        serialization_alias='https://schema.org/deliveryAddress'
    )
    itemShipped: Optional[Union['Product', List['Product']]] = Field(
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
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
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
    carrier: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'carrier',
            'https://schema.org/carrier'
        ),
        serialization_alias='https://schema.org/carrier'
    )
    deliveryStatus: Optional[Union['DeliveryEvent', List['DeliveryEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryStatus',
            'https://schema.org/deliveryStatus'
        ),
        serialization_alias='https://schema.org/deliveryStatus'
    )
    partOfOrder: Optional[Union['Order', List['Order']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfOrder',
            'https://schema.org/partOfOrder'
        ),
        serialization_alias='https://schema.org/partOfOrder'
    )
