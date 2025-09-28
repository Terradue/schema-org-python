from __future__ import annotations

from .investment_or_deposit import InvestmentOrDeposit    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BrokerageAccount(InvestmentOrDeposit):
    """
An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.
    """
    class_: Literal['https://schema.org/BrokerageAccount'] = Field( # type: ignore
        default='https://schema.org/BrokerageAccount',
        alias='@type',
        serialization_alias='@type'
    )
