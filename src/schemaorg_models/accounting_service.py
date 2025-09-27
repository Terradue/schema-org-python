from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.financial_service import FinancialService


class AccountingService(FinancialService):
    """
Accountancy business.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
      
    """
    type_: Literal['https://schema.org/AccountingService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AccountingService'),serialization_alias='class') # type: ignore
