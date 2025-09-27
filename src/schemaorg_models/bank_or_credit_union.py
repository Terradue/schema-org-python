from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class BankOrCreditUnion(FinancialService):
    """
Bank or credit union.
    """
    type_: Literal['https://schema.org/BankOrCreditUnion'] = Field(default='https://schema.org/BankOrCreditUnion', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
