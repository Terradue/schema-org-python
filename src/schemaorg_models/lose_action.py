from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.achieve_action import AchieveAction

from schemaorg_models.person import Person

class LoseAction(AchieveAction):
    """
The act of being defeated in a competitive activity.
    """
    type_: Literal['https://schema.org/LoseAction'] = Field(default='https://schema.org/LoseAction', alias='@type', serialization_alias='@type') # type: ignore
    winner: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('winner', 'https://schema.org/winner'), serialization_alias='https://schema.org/winner')
