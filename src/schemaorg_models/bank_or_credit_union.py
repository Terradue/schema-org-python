from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class BankOrCreditUnion(FinancialService):
    """
Bank or credit union.
    """
    class_: Literal['https://schema.org/BankOrCreditUnion'] = Field('class', alias='class', serialization_alias='class') # type: ignore
