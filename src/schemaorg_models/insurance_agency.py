from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class InsuranceAgency(FinancialService):
    """
An Insurance agency.
    """
    class_: Literal['https://schema.org/InsuranceAgency'] = Field('class', alias='class', serialization_alias='class') # type: ignore
