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
from .person import Person

class LendAction(TransferAction):
    """
The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.\
\
Related actions:\
\
* [[BorrowAction]]: Reciprocal of LendAction.
    """
    class_: Literal['https://schema.org/LendAction'] = Field( # type: ignore
        default='https://schema.org/LendAction',
        alias='@type',
        serialization_alias='@type'
    )
    borrower: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'borrower',
            'https://schema.org/borrower'
        ),
        serialization_alias='https://schema.org/borrower'
    )
