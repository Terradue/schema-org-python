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
    from .invoice import Invoice
    from .offer import Offer
    from .service import Service
    from .product import Product
    from .postal_address import PostalAddress
    from .organization import Organization
    from .order_item import OrderItem
    from .payment_method import PaymentMethod
    from .person import Person
    from .order_status import OrderStatus
    from .parcel_delivery import ParcelDelivery

class Order(Intangible):
    '''
    An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

    Attributes:
        orderDelivery: The delivery of the parcel related to this order or order item.
        broker: An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        isGift: Indicates whether the offer was accepted as a gift for someone other than the buyer.
        customer: Party placing the order or paying the invoice.
        paymentMethod: The name of the credit card or other method of payment for the order.
        merchant: 'merchant' is an out-dated term for 'seller'.
        discountCurrency: The currency of the discount.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        confirmationNumber: A number that confirms the given order or payment has been received.
        orderStatus: The current status of the order.
        partOfInvoice: The order is being paid as part of the referenced Invoice.
        orderNumber: The identifier of the transaction.
        acceptedOffer: The offer(s) -- e.g., product, quantity and price combinations -- included in the order.
        seller: An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        paymentDueDate: The date that payment is due.
        billingAddress: The billing address for the order.
        orderedItem: The item ordered.
        orderDate: Date order was placed.
        paymentDue: The date that payment is due.
        paymentUrl: The URL for sending a payment.
        discountCode: Code used to redeem a discount.
        paymentMethodId: An identifier for the method of payment used (e.g. the last 4 digits of the credit card).
        discount: Any discount applied (to an Order).
    '''
    class_: Literal['https://schema.org/Order'] = Field( # type: ignore
        default='https://schema.org/Order',
        alias='@type',
        serialization_alias='@type'
    )
    orderDelivery: Optional[Union['ParcelDelivery', List['ParcelDelivery']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderDelivery',
            'https://schema.org/orderDelivery'
        ),
        serialization_alias='https://schema.org/orderDelivery'
    )
    broker: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
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
    customer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customer',
            'https://schema.org/customer'
        ),
        serialization_alias='https://schema.org/customer'
    )
    paymentMethod: Optional[Union[str, List[str], 'PaymentMethod', List['PaymentMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentMethod',
            'https://schema.org/paymentMethod'
        ),
        serialization_alias='https://schema.org/paymentMethod'
    )
    merchant: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
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
    orderStatus: Optional[Union['OrderStatus', List['OrderStatus']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderStatus',
            'https://schema.org/orderStatus'
        ),
        serialization_alias='https://schema.org/orderStatus'
    )
    partOfInvoice: Optional[Union['Invoice', List['Invoice']]] = Field(
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
    acceptedOffer: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedOffer',
            'https://schema.org/acceptedOffer'
        ),
        serialization_alias='https://schema.org/acceptedOffer'
    )
    seller: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
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
    billingAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingAddress',
            'https://schema.org/billingAddress'
        ),
        serialization_alias='https://schema.org/billingAddress'
    )
    orderedItem: Optional[Union['OrderItem', List['OrderItem'], 'Service', List['Service'], 'Product', List['Product']]] = Field(
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
