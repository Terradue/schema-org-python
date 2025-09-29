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

class PaymentService(FinancialProduct):
    '''
    A Service to transfer funds from a person or organization to a beneficiary person or organization.
    '''
    class_: Literal['https://schema.org/PaymentService'] = Field( # type: ignore
        default='https://schema.org/PaymentService',
        alias='@type',
        serialization_alias='@type'
    )
