from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class InsuranceAgency(FinancialService):
    """
An Insurance agency.
    """
    type_: Literal['https://schema.org/InsuranceAgency'] = Field(default='https://schema.org/InsuranceAgency', alias='@type', serialization_alias='@type') # type: ignore
