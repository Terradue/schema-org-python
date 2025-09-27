from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class AutomatedTeller(FinancialService):
    """
ATM/cash machine.
    """
    type_: Literal['https://schema.org/AutomatedTeller'] = Field(default='https://schema.org/AutomatedTeller', alias='@type', serialization_alias='@type') # type: ignore
