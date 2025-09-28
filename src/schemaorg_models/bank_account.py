from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
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

class BankAccount(FinancialProduct):
    """
A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.
    """
    class_: Literal['https://schema.org/BankAccount'] = Field( # type: ignore
        default='https://schema.org/BankAccount',
        alias='@type',
        serialization_alias='@type'
    )
    bankAccountType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bankAccountType',
            'https://schema.org/bankAccountType'
        ),
        serialization_alias='https://schema.org/bankAccountType'
    )
    accountOverdraftLimit: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountOverdraftLimit',
            'https://schema.org/accountOverdraftLimit'
        ),
        serialization_alias='https://schema.org/accountOverdraftLimit'
    )
    accountMinimumInflow: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountMinimumInflow',
            'https://schema.org/accountMinimumInflow'
        ),
        serialization_alias='https://schema.org/accountMinimumInflow'
    )
