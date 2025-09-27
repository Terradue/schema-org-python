from typing import Literal
from pydantic import Field
from schemaorg_models.financial_service import FinancialService


class AccountingService(FinancialService):
    """
Accountancy business.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
      
    """
    class_: Literal['https://schema.org/AccountingService'] = Field(default='https://schema.org/AccountingService', alias='@type', serialization_alias='@type') # type: ignore
