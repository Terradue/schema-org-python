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
    from .invoice import Invoice
    from .postal_address import PostalAddress
    from .product import Product
    from .offer import Offer
    from .payment_method import PaymentMethod
    from .parcel_delivery import ParcelDelivery
    from .order_item import OrderItem
    from .person import Person
    from .organization import Organization
    from .service import Service
    from .order_status import OrderStatus

class Order(Intangible):
    """
An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.
    """
    class_: Literal['https://schema.org/Order'] = Field( # type: ignore
        default='https://schema.org/Order',
        alias='@type',
        serialization_alias='@type'
    )
    orderDelivery: Optional[Union["ParcelDelivery", List["ParcelDelivery"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderDelivery',
            'https://schema.org/orderDelivery'
        ),
        serialization_alias='https://schema.org/orderDelivery'
    )
    broker: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broker',
            'https://schema.org/broker'
        ),
        serialization_alias='https://schema.org/broker'
    )
    isGift: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isGift',
            'https://schema.org/isGift'
        ),
        serialization_alias='https://schema.org/isGift'
    )
    customer: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customer',
            'https://schema.org/customer'
        ),
        serialization_alias='https://schema.org/customer'
    )
    paymentMethod: Optional[Union[str, List[str], "PaymentMethod", List["PaymentMethod"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentMethod',
            'https://schema.org/paymentMethod'
        ),
        serialization_alias='https://schema.org/paymentMethod'
    )
    merchant: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchant',
            'https://schema.org/merchant'
        ),
        serialization_alias='https://schema.org/merchant'
    )
    discountCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'discountCurrency',
            'https://schema.org/discountCurrency'
        ),
        serialization_alias='https://schema.org/discountCurrency'
    )
    confirmationNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'confirmationNumber',
            'https://schema.org/confirmationNumber'
        ),
        serialization_alias='https://schema.org/confirmationNumber'
    )
    orderStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderStatus',
            'https://schema.org/orderStatus'
        ),
        serialization_alias='https://schema.org/orderStatus'
    )
    partOfInvoice: Optional[Union["Invoice", List["Invoice"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfInvoice',
            'https://schema.org/partOfInvoice'
        ),
        serialization_alias='https://schema.org/partOfInvoice'
    )
    orderNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderNumber',
            'https://schema.org/orderNumber'
        ),
        serialization_alias='https://schema.org/orderNumber'
    )
    acceptedOffer: Optional[Union["Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedOffer',
            'https://schema.org/acceptedOffer'
        ),
        serialization_alias='https://schema.org/acceptedOffer'
    )
    seller: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seller',
            'https://schema.org/seller'
        ),
        serialization_alias='https://schema.org/seller'
    )
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentDueDate',
            'https://schema.org/paymentDueDate'
        ),
        serialization_alias='https://schema.org/paymentDueDate'
    )
    billingAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingAddress',
            'https://schema.org/billingAddress'
        ),
        serialization_alias='https://schema.org/billingAddress'
    )
    orderedItem: Optional[Union["OrderItem", List["OrderItem"], "Service", List["Service"], "Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderedItem',
            'https://schema.org/orderedItem'
        ),
        serialization_alias='https://schema.org/orderedItem'
    )
    orderDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderDate',
            'https://schema.org/orderDate'
        ),
        serialization_alias='https://schema.org/orderDate'
    )
    paymentDue: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentDue',
            'https://schema.org/paymentDue'
        ),
        serialization_alias='https://schema.org/paymentDue'
    )
    paymentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentUrl',
            'https://schema.org/paymentUrl'
        ),
        serialization_alias='https://schema.org/paymentUrl'
    )
    discountCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'discountCode',
            'https://schema.org/discountCode'
        ),
        serialization_alias='https://schema.org/discountCode'
    )
    paymentMethodId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentMethodId',
            'https://schema.org/paymentMethodId'
        ),
        serialization_alias='https://schema.org/paymentMethodId'
    )
    discount: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'discount',
            'https://schema.org/discount'
        ),
        serialization_alias='https://schema.org/discount'
    )
