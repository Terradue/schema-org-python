from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.financial_service import FinancialService


class AutomatedTeller(FinancialService):
    """
ATM/cash machine.
    """
    type_: Literal['https://schema.org/AutomatedTeller'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutomatedTeller'),serialization_alias='class') # type: ignore
