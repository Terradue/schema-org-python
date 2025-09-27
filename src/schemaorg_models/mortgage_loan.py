from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.loan_or_credit import LoanOrCredit

from schemaorg_models.monetary_amount import MonetaryAmount

class MortgageLoan(LoanOrCredit):
    """
A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)
    """
    type_: Literal['https://schema.org/MortgageLoan'] = Field(default='https://schema.org/MortgageLoan', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    loanMortgageMandateAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(default=None, validation_alias=AliasChoices('loanMortgageMandateAmount', 'https://schema.org/loanMortgageMandateAmount'), serialization_alias='https://schema.org/loanMortgageMandateAmount')
    domiciledMortgage: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('domiciledMortgage', 'https://schema.org/domiciledMortgage'), serialization_alias='https://schema.org/domiciledMortgage')
