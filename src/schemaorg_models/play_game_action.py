from __future__ import annotations

from .consume_action import ConsumeAction    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.game_availability_enumeration import GameAvailabilityEnumeration

class PlayGameAction(ConsumeAction):
    """
The act of playing a video game.
    """
    class_: Literal['https://schema.org/PlayGameAction'] = Field( # type: ignore
        default='https://schema.org/PlayGameAction',
        alias='@type',
        serialization_alias='@type'
    )
    gameAvailabilityType: Optional[Union[str, List[str], GameAvailabilityEnumeration, List[GameAvailabilityEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameAvailabilityType',
            'https://schema.org/gameAvailabilityType'
        ),
        serialization_alias='https://schema.org/gameAvailabilityType'
    )
