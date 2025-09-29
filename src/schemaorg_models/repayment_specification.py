from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    A structured value representing repayment.

    Attributes:
        numberOfLoanPayments: The number of payments contractually required at origination to repay the loan. For monthly paying loans this is the number of months from the contractual first payment date to the maturity date.
        loanPaymentAmount: The amount of money to pay in a single payment.
        earlyPrepaymentPenalty: The amount to be paid as a penalty in the event of early payment of the loan.
        downPayment: a type of payment made in cash during the onset of the purchase of an expensive good/service. The payment typically represents only a percentage of the full purchase price.
        loanPaymentFrequency: Frequency of payments due, i.e. number of months between payments. This is defined as a frequency, i.e. the reciprocal of a period of time.
    '''
    class_: Literal['https://schema.org/RepaymentSpecification'] = Field( # type: ignore
        default='https://schema.org/RepaymentSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    numberOfLoanPayments: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    loanPaymentAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    earlyPrepaymentPenalty: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    downPayment: Optional[Union[float, List[float], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    loanPaymentFrequency: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
