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
    from .person import Person

class LendAction(TransferAction):
    '''
    The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.\
\
Related actions:\
\
* [[BorrowAction]]: Reciprocal of LendAction.

    Attributes:
        borrower: A sub property of participant. The person that borrows the object being lent.
    '''
    class_: Literal['https://schema.org/LendAction'] = Field( # type: ignore
        default='https://schema.org/LendAction',
        alias='@type',
        serialization_alias='@type'
    )
    borrower: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
