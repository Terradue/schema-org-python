from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.financial_product import FinancialProduct


class PaymentService(FinancialProduct):
    """
A Service to transfer funds from a person or organization to a beneficiary person or organization.
    """
    type_: Literal['https://schema.org/PaymentService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PaymentService'),serialization_alias='class') # type: ignore
