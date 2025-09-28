from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.investment_or_deposit import InvestmentOrDeposit

from pydantic import (
    Field
)
from typing import (
    Literal
)

class InvestmentFund(InvestmentOrDeposit):
    """
A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.
    """
    class_: Literal['https://schema.org/InvestmentFund'] = Field( # type: ignore
        default='https://schema.org/InvestmentFund',
        alias='@type',
        serialization_alias='@type'
    )
