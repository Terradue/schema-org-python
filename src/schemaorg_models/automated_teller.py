from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class AutomatedTeller(FinancialService):
    """
ATM/cash machine.
    """
    class_: Literal['https://schema.org/AutomatedTeller'] = Field('class', alias='class', serialization_alias='class') # type: ignore
