from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .consume_action import ConsumeAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .game_availability_enumeration import GameAvailabilityEnumeration

class PlayGameAction(ConsumeAction):
    '''
    The act of playing a video game.

    Attributes:
        gameAvailabilityType: Indicates the availability type of the game content associated with this action, such as whether it is a full version or a demo.
    '''
    class_: Literal['https://schema.org/PlayGameAction'] = Field( # type: ignore
        default='https://schema.org/PlayGameAction',
        alias='@type',
        serialization_alias='@type'
    )
    gameAvailabilityType: Optional[Union[str, List[str], 'GameAvailabilityEnumeration', List['GameAvailabilityEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
