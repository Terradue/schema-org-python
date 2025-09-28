from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .financial_service import FinancialService

class InsuranceAgency(FinancialService):
    """
An Insurance agency.
    """
    class_: Literal['https://schema.org/InsuranceAgency'] = Field( # type: ignore
        default='https://schema.org/InsuranceAgency',
        alias='@type',
        serialization_alias='@type'
    )
