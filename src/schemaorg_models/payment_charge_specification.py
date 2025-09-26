from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.price_specification import PriceSpecification

from schemaorg_models.delivery_method import DeliveryMethod
from schemaorg_models.payment_method import PaymentMethod

class PaymentChargeSpecification(PriceSpecification):
    """
The costs of settling the payment using a particular payment method.
    """
    appliesToDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None,validation_alias=AliasChoices('appliesToDeliveryMethod', 'https://schema.org/appliesToDeliveryMethod'),serialization_alias='https://schema.org/appliesToDeliveryMethod')
    appliesToPaymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = Field(default=None,validation_alias=AliasChoices('appliesToPaymentMethod', 'https://schema.org/appliesToPaymentMethod'),serialization_alias='https://schema.org/appliesToPaymentMethod')
