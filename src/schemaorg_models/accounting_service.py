from __future__ import annotations

from .financial_service import FinancialService    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AccountingService(FinancialService):
    """
Accountancy business.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
      
    """
    class_: Literal['https://schema.org/AccountingService'] = Field( # type: ignore
        default='https://schema.org/AccountingService',
        alias='@type',
        serialization_alias='@type'
    )
