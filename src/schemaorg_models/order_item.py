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
    from .service import Service
    from .product import Product
    from .parcel_delivery import ParcelDelivery
    from .order_status import OrderStatus
    from .quantitative_value import QuantitativeValue

class OrderItem(Intangible):
    '''
    An order item is a line of an order. It includes the quantity and shipping details of a bought offer.

    Attributes:
        orderQuantity: The number of the item ordered. If the property is not set, assume the quantity is one.
        orderItemStatus: The current status of the order item.
        orderItemNumber: The identifier of the order item.
        orderDelivery: The delivery of the parcel related to this order or order item.
        orderedItem: The item ordered.
    '''
    class_: Literal['https://schema.org/OrderItem'] = Field( # type: ignore
        default='https://schema.org/OrderItem',
        alias='@type',
        serialization_alias='@type'
    )
    orderQuantity: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    orderItemStatus: Optional[Union['OrderStatus', List['OrderStatus']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    orderItemNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    orderDelivery: Optional[Union['ParcelDelivery', List['ParcelDelivery']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    orderedItem: Optional[Union['OrderItem', List['OrderItem'], 'Service', List['Service'], 'Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
