from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.achieve_action import AchieveAction

from schemaorg_models.person import Person

class LoseAction(AchieveAction):
    """
The act of being defeated in a competitive activity.
    """
    class_: Literal['https://schema.org/LoseAction'] = Field(default='https://schema.org/LoseAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    winner: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('winner', 'https://schema.org/winner'), serialization_alias='https://schema.org/winner')
