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
from .transfer_action import TransferAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .bank_or_credit_union import BankOrCreditUnion
    from .monetary_amount import MonetaryAmount

class MoneyTransfer(TransferAction):
    """
The act of transferring money from one place to another place. This may occur electronically or physically.
    """
    class_: Literal['https://schema.org/MoneyTransfer'] = Field( # type: ignore
        default='https://schema.org/MoneyTransfer',
        alias='@type',
        serialization_alias='@type'
    )
    beneficiaryBank: Optional[Union[str, List[str], BankOrCreditUnion, List[BankOrCreditUnion]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'beneficiaryBank',
            'https://schema.org/beneficiaryBank'
        ),
        serialization_alias='https://schema.org/beneficiaryBank'
    )
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amount',
            'https://schema.org/amount'
        ),
        serialization_alias='https://schema.org/amount'
    )
