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
from .financial_product import FinancialProduct
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

class BankAccount(FinancialProduct):
    '''
    A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.

    Attributes:
        bankAccountType: The type of a bank account.
        accountOverdraftLimit: An overdraft is an extension of credit from a lending institution when an account reaches zero. An overdraft allows the individual to continue withdrawing money even if the account has no funds in it. Basically the bank allows people to borrow a set amount of money.
        accountMinimumInflow: A minimum amount that has to be paid in every month.
    '''
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
    accountOverdraftLimit: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountOverdraftLimit',
            'https://schema.org/accountOverdraftLimit'
        ),
        serialization_alias='https://schema.org/accountOverdraftLimit'
    )
    accountMinimumInflow: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountMinimumInflow',
            'https://schema.org/accountMinimumInflow'
        ),
        serialization_alias='https://schema.org/accountMinimumInflow'
    )
