from typing import Literal
from pydantic import Field
from schemaorg_models.investment_or_deposit import InvestmentOrDeposit


class DepositAccount(InvestmentOrDeposit):
    """
A type of Bank Account with a main purpose of depositing funds to gain interest or other benefits.
    """
    type_: Literal['https://schema.org/DepositAccount'] = Field(default='https://schema.org/DepositAccount', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
