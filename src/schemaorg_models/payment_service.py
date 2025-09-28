from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.financial_product import FinancialProduct

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PaymentService(FinancialProduct):
    """
A Service to transfer funds from a person or organization to a beneficiary person or organization.
    """
    class_: Literal['https://schema.org/PaymentService'] = Field( # type: ignore
        default='https://schema.org/PaymentService',
        alias='@type',
        serialization_alias='@type'
    )
