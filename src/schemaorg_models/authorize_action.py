from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.allocate_action import AllocateAction

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class AuthorizeAction(AllocateAction):
    """
The act of granting permission to an object.
    """
    type_: Literal['https://schema.org/AuthorizeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AuthorizeAction'),serialization_alias='class') # type: ignore
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'),serialization_alias='https://schema.org/recipient')
