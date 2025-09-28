from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.loan_or_credit import LoanOrCredit

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
from schemaorg_models.monetary_amount import MonetaryAmount

class MortgageLoan(LoanOrCredit):
    """
A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)
    """
    class_: Literal['https://schema.org/MortgageLoan'] = Field( # type: ignore
        default='https://schema.org/MortgageLoan',
        alias='@type',
        serialization_alias='@type'
    )
    loanMortgageMandateAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loanMortgageMandateAmount',
            'https://schema.org/loanMortgageMandateAmount'
        ),
        serialization_alias='https://schema.org/loanMortgageMandateAmount'
    )
    domiciledMortgage: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'domiciledMortgage',
            'https://schema.org/domiciledMortgage'
        ),
        serialization_alias='https://schema.org/domiciledMortgage'
    )
