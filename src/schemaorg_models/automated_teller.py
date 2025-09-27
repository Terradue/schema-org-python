from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class AutomatedTeller(FinancialService):
    """
ATM/cash machine.
    """
    class_: Literal['https://schema.org/AutomatedTeller'] = Field(default='https://schema.org/AutomatedTeller', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
