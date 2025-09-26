from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction

from schemaorg_models.game_availability_enumeration import GameAvailabilityEnumeration

class PlayGameAction(ConsumeAction):
    """
The act of playing a video game.
    """
    gameAvailabilityType: Optional[Union[str, List[str], GameAvailabilityEnumeration, List[GameAvailabilityEnumeration]]] = Field(default=None,validation_alias=AliasChoices('gameAvailabilityType', 'https://schema.org/gameAvailabilityType'),serialization_alias='https://schema.org/gameAvailabilityType')
