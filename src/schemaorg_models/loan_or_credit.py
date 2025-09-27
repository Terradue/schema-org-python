from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.financial_product import FinancialProduct

from schemaorg_models.duration import Duration
from schemaorg_models.thing import Thing
from schemaorg_models.repayment_specification import RepaymentSpecification
from schemaorg_models.monetary_amount import MonetaryAmount
from schemaorg_models.quantitative_value import QuantitativeValue

class LoanOrCredit(FinancialProduct):
    """
A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.
    """
    class_: Literal['https://schema.org/LoanOrCredit'] = Field(default='https://schema.org/LoanOrCredit', alias='@type', serialization_alias='@type') # type: ignore
    gracePeriod: Optional[Union[Duration, List[Duration]]] = Field(default=None, validation_alias=AliasChoices('gracePeriod', 'https://schema.org/gracePeriod'), serialization_alias='https://schema.org/gracePeriod')
    requiredCollateral: Optional[Union[str, List[str], Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('requiredCollateral', 'https://schema.org/requiredCollateral'), serialization_alias='https://schema.org/requiredCollateral')
    currency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('currency', 'https://schema.org/currency'), serialization_alias='https://schema.org/currency')
    loanRepaymentForm: Optional[Union[RepaymentSpecification, List[RepaymentSpecification]]] = Field(default=None, validation_alias=AliasChoices('loanRepaymentForm', 'https://schema.org/loanRepaymentForm'), serialization_alias='https://schema.org/loanRepaymentForm')
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('amount', 'https://schema.org/amount'), serialization_alias='https://schema.org/amount')
    recourseLoan: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('recourseLoan', 'https://schema.org/recourseLoan'), serialization_alias='https://schema.org/recourseLoan')
    loanTerm: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('loanTerm', 'https://schema.org/loanTerm'), serialization_alias='https://schema.org/loanTerm')
    loanType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('loanType', 'https://schema.org/loanType'), serialization_alias='https://schema.org/loanType')
    @field_serializer('loanType')
    def loanType2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    renegotiableLoan: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('renegotiableLoan', 'https://schema.org/renegotiableLoan'), serialization_alias='https://schema.org/renegotiableLoan')
