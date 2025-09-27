from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue


class RepaymentSpecification(StructuredValue):
    """
A structured value representing repayment.
    """
    type_: Literal['https://schema.org/RepaymentSpecification'] = Field(default='https://schema.org/RepaymentSpecification', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    numberOfLoanPayments: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('numberOfLoanPayments', 'https://schema.org/numberOfLoanPayments'), serialization_alias='https://schema.org/numberOfLoanPayments')
    loanPaymentAmount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('loanPaymentAmount', 'https://schema.org/loanPaymentAmount'), serialization_alias='https://schema.org/loanPaymentAmount')
    earlyPrepaymentPenalty: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('earlyPrepaymentPenalty', 'https://schema.org/earlyPrepaymentPenalty'), serialization_alias='https://schema.org/earlyPrepaymentPenalty')
    downPayment: Optional[Union[float, List[float], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('downPayment', 'https://schema.org/downPayment'), serialization_alias='https://schema.org/downPayment')
    loanPaymentFrequency: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('loanPaymentFrequency', 'https://schema.org/loanPaymentFrequency'), serialization_alias='https://schema.org/loanPaymentFrequency')
