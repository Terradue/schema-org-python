from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.choose_action import ChooseAction

from schemaorg_models.person import Person

class VoteAction(ChooseAction):
    """
The act of expressing a preference from a fixed/finite/structured set of choices/options.
    """
    candidate: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('candidate', 'https://schema.org/candidate'),serialization_alias='https://schema.org/candidate')
