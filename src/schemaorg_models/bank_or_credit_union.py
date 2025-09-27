from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class BankOrCreditUnion(FinancialService):
    """
Bank or credit union.
    """
    class_: Literal['https://schema.org/BankOrCreditUnion'] = Field(default='https://schema.org/BankOrCreditUnion', alias='@type', serialization_alias='@type') # type: ignore
