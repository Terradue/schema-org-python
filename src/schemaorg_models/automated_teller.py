from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .financial_service import FinancialService

class AutomatedTeller(FinancialService):
    """
ATM/cash machine.
    """
    class_: Literal['https://schema.org/AutomatedTeller'] = Field( # type: ignore
        default='https://schema.org/AutomatedTeller',
        alias='@type',
        serialization_alias='@type'
    )
