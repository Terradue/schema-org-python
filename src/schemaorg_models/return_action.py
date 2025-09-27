from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class ReturnAction(TransferAction):
    """
The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).
    """
    type_: Literal['https://schema.org/ReturnAction'] = Field(default='https://schema.org/ReturnAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'), serialization_alias='https://schema.org/recipient')
