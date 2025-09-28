from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .financial_service import FinancialService

class BankOrCreditUnion(FinancialService):
    """
Bank or credit union.
    """
    class_: Literal['https://schema.org/BankOrCreditUnion'] = Field( # type: ignore
        default='https://schema.org/BankOrCreditUnion',
        alias='@type',
        serialization_alias='@type'
    )
