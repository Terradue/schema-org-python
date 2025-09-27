from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.financial_product import FinancialProduct

from schemaorg_models.monetary_amount import MonetaryAmount

class InvestmentOrDeposit(FinancialProduct):
    """
A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.
    """
    type_: Literal['https://schema.org/InvestmentOrDeposit'] = Field(default='https://schema.org/InvestmentOrDeposit', alias='@type', serialization_alias='@type') # type: ignore
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('amount', 'https://schema.org/amount'), serialization_alias='https://schema.org/amount')
