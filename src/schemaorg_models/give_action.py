from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class GiveAction(TransferAction):
    """
The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.\
\
Related actions:\
\
* [[TakeAction]]: Reciprocal of GiveAction.\
* [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).
    """
    class_: Literal['https://schema.org/GiveAction'] = Field(default='https://schema.org/GiveAction', alias='@type', serialization_alias='@type') # type: ignore
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'), serialization_alias='https://schema.org/recipient')
