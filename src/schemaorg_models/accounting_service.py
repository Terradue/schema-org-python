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

class AccountingService(FinancialService):
    '''
    Accountancy business.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
      
    '''
    class_: Literal['https://schema.org/AccountingService'] = Field( # type: ignore
        default='https://schema.org/AccountingService',
        alias='@type',
        serialization_alias='@type'
    )
