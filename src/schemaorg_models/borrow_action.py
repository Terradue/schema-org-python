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
    from .organization import Organization
    from .person import Person

class BorrowAction(TransferAction):
    """
The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.\
\
Related actions:\
\
* [[LendAction]]: Reciprocal of BorrowAction.
    """
    class_: Literal['https://schema.org/BorrowAction'] = Field( # type: ignore
        default='https://schema.org/BorrowAction',
        alias='@type',
        serialization_alias='@type'
    )
    lender: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lender',
            'https://schema.org/lender'
        ),
        serialization_alias='https://schema.org/lender'
    )
