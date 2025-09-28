from __future__ import annotations

from .financial_service import FinancialService    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class InsuranceAgency(FinancialService):
    """
An Insurance agency.
    """
    class_: Literal['https://schema.org/InsuranceAgency'] = Field( # type: ignore
        default='https://schema.org/InsuranceAgency',
        alias='@type',
        serialization_alias='@type'
    )
