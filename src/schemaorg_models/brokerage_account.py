from typing import Literal
from pydantic import Field
from schemaorg_models.investment_or_deposit import InvestmentOrDeposit


class BrokerageAccount(InvestmentOrDeposit):
    """
An account that allows an investor to deposit funds and place investment orders with a licensed broker or brokerage firm.
    """
    class_: Literal['https://schema.org/BrokerageAccount'] = Field(default='https://schema.org/BrokerageAccount', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
