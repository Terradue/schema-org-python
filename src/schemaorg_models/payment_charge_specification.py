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
    from .payment_method import PaymentMethod
    from .delivery_method import DeliveryMethod

class PaymentChargeSpecification(PriceSpecification):
    '''
    The costs of settling the payment using a particular payment method.

    Attributes:
        appliesToDeliveryMethod: The delivery method(s) to which the delivery charge or payment charge specification applies.
        appliesToPaymentMethod: The payment method(s) to which the payment charge specification applies.
    '''
    class_: Literal['https://schema.org/PaymentChargeSpecification'] = Field( # type: ignore
        default='https://schema.org/PaymentChargeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    appliesToDeliveryMethod: Optional[Union['DeliveryMethod', List['DeliveryMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToDeliveryMethod',
            'https://schema.org/appliesToDeliveryMethod'
        ),
        serialization_alias='https://schema.org/appliesToDeliveryMethod'
    )
    appliesToPaymentMethod: Optional[Union['PaymentMethod', List['PaymentMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToPaymentMethod',
            'https://schema.org/appliesToPaymentMethod'
        ),
        serialization_alias='https://schema.org/appliesToPaymentMethod'
    )
