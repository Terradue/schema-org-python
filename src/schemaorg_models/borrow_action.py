from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class BorrowAction(TransferAction):
    """
The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction.\
\
Related actions:\
\
* [[LendAction]]: Reciprocal of BorrowAction.
    """
    type_: Literal['https://schema.org/BorrowAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BorrowAction'),serialization_alias='class') # type: ignore
    lender: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('lender', 'https://schema.org/lender'),serialization_alias='https://schema.org/lender')
