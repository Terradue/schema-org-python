from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class InsuranceAgency(FinancialService):
    """
An Insurance agency.
    """
    class_: Literal['https://schema.org/InsuranceAgency'] = Field(default='https://schema.org/InsuranceAgency', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
