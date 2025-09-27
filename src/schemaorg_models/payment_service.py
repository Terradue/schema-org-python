from typing import Literal
from pydantic import Field
from schemaorg_models.financial_product import FinancialProduct


class PaymentService(FinancialProduct):
    """
A Service to transfer funds from a person or organization to a beneficiary person or organization.
    """
    class_: Literal['https://schema.org/PaymentService'] = Field(default='https://schema.org/PaymentService', alias='class', serialization_alias='class') # type: ignore
