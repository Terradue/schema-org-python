from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.choose_action import ChooseAction

from schemaorg_models.person import Person

class VoteAction(ChooseAction):
    """
The act of expressing a preference from a fixed/finite/structured set of choices/options.
    """
    class_: Literal['https://schema.org/VoteAction'] = Field(default='https://schema.org/VoteAction', alias='class', serialization_alias='class') # type: ignore
    candidate: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('candidate', 'https://schema.org/candidate'), serialization_alias='https://schema.org/candidate')
