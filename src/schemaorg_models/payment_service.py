from __future__ import annotations

from .financial_product import FinancialProduct    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PaymentService(FinancialProduct):
    """
A Service to transfer funds from a person or organization to a beneficiary person or organization.
    """
    class_: Literal['https://schema.org/PaymentService'] = Field( # type: ignore
        default='https://schema.org/PaymentService',
        alias='@type',
        serialization_alias='@type'
    )
