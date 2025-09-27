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
    type_: Literal['https://schema.org/LendAction'] = Field(default='https://schema.org/LendAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    borrower: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('borrower', 'https://schema.org/borrower'), serialization_alias='https://schema.org/borrower')
