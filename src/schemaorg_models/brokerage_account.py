from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.investment_or_deposit import InvestmentOrDeposit


class BrokerageAccount(InvestmentOrDeposit):
    """
An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.
    """
    type_: Literal['https://schema.org/BrokerageAccount'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BrokerageAccount'),serialization_alias='class') # type: ignore
