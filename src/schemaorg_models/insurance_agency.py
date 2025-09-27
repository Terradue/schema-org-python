from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.financial_service import FinancialService


class InsuranceAgency(FinancialService):
    """
An Insurance agency.
    """
    type_: Literal['https://schema.org/InsuranceAgency'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InsuranceAgency'),serialization_alias='class') # type: ignore
