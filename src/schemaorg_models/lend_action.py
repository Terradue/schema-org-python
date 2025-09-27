from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.person import Person

class LendAction(TransferAction):
    """
The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.\
\
Related actions:\
\
* [[BorrowAction]]: Reciprocal of LendAction.
    """
    class_: Literal['https://schema.org/LendAction'] = Field(default='https://schema.org/LendAction', alias='class', serialization_alias='class') # type: ignore
    borrower: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('borrower', 'https://schema.org/borrower'), serialization_alias='https://schema.org/borrower')
