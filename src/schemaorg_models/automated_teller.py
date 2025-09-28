from __future__ import annotations

from .financial_service import FinancialService    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutomatedTeller(FinancialService):
    """
ATM/cash machine.
    """
    class_: Literal['https://schema.org/AutomatedTeller'] = Field( # type: ignore
        default='https://schema.org/AutomatedTeller',
        alias='@type',
        serialization_alias='@type'
    )
