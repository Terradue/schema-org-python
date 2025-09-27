from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.move_action import MoveAction

from schemaorg_models.distance import Distance

class TravelAction(MoveAction):
    """
The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.
    """
    type_: Literal['https://schema.org/TravelAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TravelAction'),serialization_alias='class') # type: ignore
    distance: Optional[Union[Distance, List[Distance]]] = Field(default=None,validation_alias=AliasChoices('distance', 'https://schema.org/distance'),serialization_alias='https://schema.org/distance')
