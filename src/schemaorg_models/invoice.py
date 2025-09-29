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
    from .thing import Thing
    from .payment_status_type import PaymentStatusType
    from .physical_activity_category import PhysicalActivityCategory
    from .category_code import CategoryCode
    from .organization import Organization
    from .duration import Duration
    from .order import Order
    from .payment_method import PaymentMethod
    from .person import Person
    from .monetary_amount import MonetaryAmount
    from .price_specification import PriceSpecification

class Invoice(Intangible):
    '''
    A statement of the money due for goods or services; a bill.

    Attributes:
        referencesOrder: The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.
        paymentDueDate: The date that payment is due.
        paymentDue: The date that payment is due.
        paymentMethodId: An identifier for the method of payment used (e.g. the last 4 digits of the credit card).
        broker: An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        accountId: The identifier for the account the payment will be applied to.
        category: A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        scheduledPaymentDate: The date the invoice is scheduled to be paid.
        totalPaymentDue: The total amount due.
        customer: Party placing the order or paying the invoice.
        paymentMethod: The name of the credit card or other method of payment for the order.
        minimumPaymentDue: The minimum payment required at this time.
        confirmationNumber: A number that confirms the given order or payment has been received.
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        paymentStatus: The status of payment; whether the invoice has been paid or not.
        billingPeriod: The time interval used to compute the invoice.
    '''
    class_: Literal['https://schema.org/Invoice'] = Field( # type: ignore
        default='https://schema.org/Invoice',
        alias='@type',
        serialization_alias='@type'
    )
    referencesOrder: Optional[Union['Order', List['Order']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'referencesOrder',
            'https://schema.org/referencesOrder'
        ),
        serialization_alias='https://schema.org/referencesOrder'
    )
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentDueDate',
            'https://schema.org/paymentDueDate'
        ),
        serialization_alias='https://schema.org/paymentDueDate'
    )
    paymentDue: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentDue',
            'https://schema.org/paymentDue'
        ),
        serialization_alias='https://schema.org/paymentDue'
    )
    paymentMethodId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentMethodId',
            'https://schema.org/paymentMethodId'
        ),
        serialization_alias='https://schema.org/paymentMethodId'
    )
    broker: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broker',
            'https://schema.org/broker'
        ),
        serialization_alias='https://schema.org/broker'
    )
    accountId: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountId',
            'https://schema.org/accountId'
        ),
        serialization_alias='https://schema.org/accountId'
    )
    category: Optional[Union['PhysicalActivityCategory', List['PhysicalActivityCategory'], 'CategoryCode', List['CategoryCode'], str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
    scheduledPaymentDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'scheduledPaymentDate',
            'https://schema.org/scheduledPaymentDate'
        ),
        serialization_alias='https://schema.org/scheduledPaymentDate'
    )
    totalPaymentDue: Optional[Union['PriceSpecification', List['PriceSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalPaymentDue',
            'https://schema.org/totalPaymentDue'
        ),
        serialization_alias='https://schema.org/totalPaymentDue'
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
    minimumPaymentDue: Optional[Union['PriceSpecification', List['PriceSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'minimumPaymentDue',
            'https://schema.org/minimumPaymentDue'
        ),
        serialization_alias='https://schema.org/minimumPaymentDue'
    )
    confirmationNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'confirmationNumber',
            'https://schema.org/confirmationNumber'
        ),
        serialization_alias='https://schema.org/confirmationNumber'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    paymentStatus: Optional[Union[str, List[str], 'PaymentStatusType', List['PaymentStatusType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentStatus',
            'https://schema.org/paymentStatus'
        ),
        serialization_alias='https://schema.org/paymentStatus'
    )
    billingPeriod: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingPeriod',
            'https://schema.org/billingPeriod'
        ),
        serialization_alias='https://schema.org/billingPeriod'
    )
