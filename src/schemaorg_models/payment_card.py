from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .financial_product import FinancialProduct
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

class PaymentCard(FinancialProduct):
    """
A payment method using a credit, debit, store or other card to associate the payment with an account.
    """
    class_: Literal['https://schema.org/PaymentCard'] = Field( # type: ignore
        default='https://schema.org/PaymentCard',
        alias='@type',
        serialization_alias='@type'
    )
    monthlyMinimumRepaymentAmount: Optional[Union[float, List[float], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'monthlyMinimumRepaymentAmount',
            'https://schema.org/monthlyMinimumRepaymentAmount'
        ),
        serialization_alias='https://schema.org/monthlyMinimumRepaymentAmount'
    )
    floorLimit: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'floorLimit',
            'https://schema.org/floorLimit'
        ),
        serialization_alias='https://schema.org/floorLimit'
    )
    cashBack: Optional[Union[float, List[float], bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cashBack',
            'https://schema.org/cashBack'
        ),
        serialization_alias='https://schema.org/cashBack'
    )
    contactlessPayment: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactlessPayment',
            'https://schema.org/contactlessPayment'
        ),
        serialization_alias='https://schema.org/contactlessPayment'
    )
