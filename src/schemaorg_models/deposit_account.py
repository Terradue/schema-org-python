from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .investment_or_deposit import InvestmentOrDeposit

class DepositAccount(InvestmentOrDeposit):
    """
A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.
    """
    class_: Literal['https://schema.org/DepositAccount'] = Field( # type: ignore
        default='https://schema.org/DepositAccount',
        alias='@type',
        serialization_alias='@type'
    )
