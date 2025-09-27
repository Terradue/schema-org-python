from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class PaymentMethodType(Enumeration):
    """
The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod.
    """
    type_: Literal['https://schema.org/PaymentMethodType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PaymentMethodType'),serialization_alias='class') # type: ignore
