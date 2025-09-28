from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .payment_method import PaymentMethod
from .delivery_method import DeliveryMethod
from .price_specification import PriceSpecification

class PaymentChargeSpecification(PriceSpecification):
    """
The costs of settling the payment using a particular payment method.
    """
    class_: Literal['https://schema.org/PaymentChargeSpecification'] = Field( # type: ignore
        default='https://schema.org/PaymentChargeSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToDeliveryMethod',
            'https://schema.org/appliesToDeliveryMethod'
        ),
        serialization_alias='https://schema.org/appliesToDeliveryMethod'
    )
    appliesToPaymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToPaymentMethod',
            'https://schema.org/appliesToPaymentMethod'
        ),
        serialization_alias='https://schema.org/appliesToPaymentMethod'
    )
