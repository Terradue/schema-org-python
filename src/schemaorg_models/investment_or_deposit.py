from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.financial_product import FinancialProduct

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.monetary_amount import MonetaryAmount

class InvestmentOrDeposit(FinancialProduct):
    """
A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.
    """
    class_: Literal['https://schema.org/InvestmentOrDeposit'] = Field( # type: ignore
        default='https://schema.org/InvestmentOrDeposit',
        alias='@type',
        serialization_alias='@type'
    )
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amount',
            'https://schema.org/amount'
        ),
        serialization_alias='https://schema.org/amount'
    )
