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
    from .quantitative_value import QuantitativeValue
    from .product import Product
    from .service import Service
    from .order_status import OrderStatus
    from .parcel_delivery import ParcelDelivery

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
            'orderQuantity',
            'https://schema.org/orderQuantity'
        ),
        serialization_alias='https://schema.org/orderQuantity'
    )
    orderItemStatus: Optional[Union['OrderStatus', List['OrderStatus']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderItemStatus',
            'https://schema.org/orderItemStatus'
        ),
        serialization_alias='https://schema.org/orderItemStatus'
    )
    orderItemNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderItemNumber',
            'https://schema.org/orderItemNumber'
        ),
        serialization_alias='https://schema.org/orderItemNumber'
    )
    orderDelivery: Optional[Union['ParcelDelivery', List['ParcelDelivery']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderDelivery',
            'https://schema.org/orderDelivery'
        ),
        serialization_alias='https://schema.org/orderDelivery'
    )
    orderedItem: Optional[Union['OrderItem', List['OrderItem'], 'Service', List['Service'], 'Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderedItem',
            'https://schema.org/orderedItem'
        ),
        serialization_alias='https://schema.org/orderedItem'
    )
