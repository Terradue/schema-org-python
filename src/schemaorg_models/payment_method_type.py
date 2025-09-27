from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PaymentMethodType(Enumeration):
    """
The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod.
    """
    class_: Literal['https://schema.org/PaymentMethodType'] = Field('class', alias='class', serialization_alias='class') # type: ignore
