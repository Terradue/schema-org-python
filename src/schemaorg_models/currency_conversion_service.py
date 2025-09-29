from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .financial_product import FinancialProduct

class CurrencyConversionService(FinancialProduct):
    '''
    A service to convert funds from one currency to another currency.
    '''
    class_: Literal['https://schema.org/CurrencyConversionService'] = Field( # type: ignore
        default='https://schema.org/CurrencyConversionService',
        alias='@type',
        serialization_alias='@type'
    )
