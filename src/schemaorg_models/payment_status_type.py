from __future__ import annotations

from .status_enumeration import StatusEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PaymentStatusType(StatusEnumeration):
    """
A specific payment status. For example, PaymentDue, PaymentComplete, etc.
    """
    class_: Literal['https://schema.org/PaymentStatusType'] = Field( # type: ignore
        default='https://schema.org/PaymentStatusType',
        alias='@type',
        serialization_alias='@type'
    )
