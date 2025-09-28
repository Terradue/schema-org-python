from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .financial_product import FinancialProduct

class CurrencyConversionService(FinancialProduct):
    """
A service to convert funds from one currency to another currency.
    """
    class_: Literal['https://schema.org/CurrencyConversionService'] = Field( # type: ignore
        default='https://schema.org/CurrencyConversionService',
        alias='@type',
        serialization_alias='@type'
    )
