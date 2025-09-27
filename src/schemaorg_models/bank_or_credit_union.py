from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.financial_service import FinancialService


class BankOrCreditUnion(FinancialService):
    """
Bank or credit union.
    """
    type_: Literal['https://schema.org/BankOrCreditUnion'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BankOrCreditUnion'),serialization_alias='class') # type: ignore
