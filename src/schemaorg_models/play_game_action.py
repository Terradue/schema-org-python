from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction

from schemaorg_models.game_availability_enumeration import GameAvailabilityEnumeration

class PlayGameAction(ConsumeAction):
    """
The act of playing a video game.
    """
    class_: Literal['https://schema.org/PlayGameAction'] = Field(default='https://schema.org/PlayGameAction', alias='class', serialization_alias='class') # type: ignore
    gameAvailabilityType: Optional[Union[str, List[str], GameAvailabilityEnumeration, List[GameAvailabilityEnumeration]]] = Field(default=None, validation_alias=AliasChoices('gameAvailabilityType', 'https://schema.org/gameAvailabilityType'), serialization_alias='https://schema.org/gameAvailabilityType')
