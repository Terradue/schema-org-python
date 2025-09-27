from typing import Literal
from pydantic import Field
from schemaorg_models.investment_or_deposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """
A company or fund that gathers capital from a number of investors to create a pool of money that is then re-invested into stocks, bonds and other assets.
    """
    type_: Literal['https://schema.org/InvestmentFund'] = Field(default='https://schema.org/InvestmentFund', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
