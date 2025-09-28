from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .financial_product import FinancialProduct

class PaymentService(FinancialProduct):
    """
A Service to transfer funds from a person or organization to a beneficiary person or organization.
    """
    class_: Literal['https://schema.org/PaymentService'] = Field( # type: ignore
        default='https://schema.org/PaymentService',
        alias='@type',
        serialization_alias='@type'
    )
