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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

class RepaymentSpecification(StructuredValue):
    """
A structured value representing repayment.
    """
    class_: Literal['https://schema.org/RepaymentSpecification'] = Field( # type: ignore
        default='https://schema.org/RepaymentSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfLoanPayments: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfLoanPayments',
            'https://schema.org/numberOfLoanPayments'
        ),
        serialization_alias='https://schema.org/numberOfLoanPayments'
    )
    loanPaymentAmount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loanPaymentAmount',
            'https://schema.org/loanPaymentAmount'
        ),
        serialization_alias='https://schema.org/loanPaymentAmount'
    )
    earlyPrepaymentPenalty: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'earlyPrepaymentPenalty',
            'https://schema.org/earlyPrepaymentPenalty'
        ),
        serialization_alias='https://schema.org/earlyPrepaymentPenalty'
    )
    downPayment: Optional[Union[float, List[float], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'downPayment',
            'https://schema.org/downPayment'
        ),
        serialization_alias='https://schema.org/downPayment'
    )
    loanPaymentFrequency: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loanPaymentFrequency',
            'https://schema.org/loanPaymentFrequency'
        ),
        serialization_alias='https://schema.org/loanPaymentFrequency'
    )
