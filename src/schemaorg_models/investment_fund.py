from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.investment_or_deposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """
A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.
    """
    type_: Literal['https://schema.org/InvestmentFund'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InvestmentFund'),serialization_alias='class') # type: ignore
