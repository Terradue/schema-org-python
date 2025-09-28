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

class BankOrCreditUnion(FinancialService):
    """
Bank or credit union.
    """
    class_: Literal['https://schema.org/BankOrCreditUnion'] = Field( # type: ignore
        default='https://schema.org/BankOrCreditUnion',
        alias='@type',
        serialization_alias='@type'
    )
