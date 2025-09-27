from typing import Literal
from pydantic import Field
from schemaorg_models.investment_or_deposit import InvestmentOrDeposit


class DepositAccount(InvestmentOrDeposit):
    """
A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.
    """
    class_: Literal['https://schema.org/DepositAccount'] = Field('class', alias='class', serialization_alias='class') # type: ignore
