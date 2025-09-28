from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.financial_service import FinancialService

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
