from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.price_specification import PriceSpecification

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
from schemaorg_models.delivery_method import DeliveryMethod
from schemaorg_models.payment_method import PaymentMethod

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
