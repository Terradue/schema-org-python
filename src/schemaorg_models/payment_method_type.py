from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class PaymentMethodType(Enumeration):
    """
The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod.
    """
    class_: Literal['https://schema.org/PaymentMethodType'] = Field( # type: ignore
        default='https://schema.org/PaymentMethodType',
        alias='@type',
        serialization_alias='@type'
    )
