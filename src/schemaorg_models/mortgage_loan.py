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
from .loan_or_credit import LoanOrCredit
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

class MortgageLoan(LoanOrCredit):
    '''
    A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

    Attributes:
        loanMortgageMandateAmount: Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.
        domiciledMortgage: Whether borrower is a resident of the jurisdiction where the property is located.
    '''
    class_: Literal['https://schema.org/MortgageLoan'] = Field( # type: ignore
        default='https://schema.org/MortgageLoan',
        alias='@type',
        serialization_alias='@type'
    )
    loanMortgageMandateAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
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
