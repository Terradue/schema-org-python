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
from .financial_service import FinancialService

class BankOrCreditUnion(FinancialService):
    '''
    Bank or credit union.
    '''
    class_: Literal['https://schema.org/BankOrCreditUnion'] = Field( # type: ignore
        default='https://schema.org/BankOrCreditUnion',
        alias='@type',
        serialization_alias='@type'
    )
