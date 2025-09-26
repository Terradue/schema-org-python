from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.react_action import ReactAction

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class EndorseAction(ReactAction):
    """
An agent approves/certifies/likes/supports/sanctions an object.
    """
    endorsee: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('endorsee', 'https://schema.org/endorsee'),serialization_alias='https://schema.org/endorsee')
