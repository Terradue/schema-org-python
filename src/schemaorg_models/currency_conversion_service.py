from __future__ import annotations

from .financial_product import FinancialProduct    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CurrencyConversionService(FinancialProduct):
    """
A service to convert funds from one currency to another currency.
    """
    class_: Literal['https://schema.org/CurrencyConversionService'] = Field( # type: ignore
        default='https://schema.org/CurrencyConversionService',
        alias='@type',
        serialization_alias='@type'
    )
