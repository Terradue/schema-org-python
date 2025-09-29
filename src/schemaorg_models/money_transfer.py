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
from .transfer_action import TransferAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .bank_or_credit_union import BankOrCreditUnion

class MoneyTransfer(TransferAction):
    '''
    The act of transferring money from one place to another place. This may occur electronically or physically.

    Attributes:
        beneficiaryBank: A bank or bank’s branch, financial institution or international financial institution operating the beneficiary’s bank account or releasing funds for the beneficiary.
        amount: The amount of money.
    '''
    class_: Literal['https://schema.org/MoneyTransfer'] = Field( # type: ignore
        default='https://schema.org/MoneyTransfer',
        alias='@type',
        serialization_alias='@type'
    )
    beneficiaryBank: Optional[Union[str, List[str], 'BankOrCreditUnion', List['BankOrCreditUnion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    amount: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
