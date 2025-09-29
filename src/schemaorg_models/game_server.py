from __future__ import annotations
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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .video_game import VideoGame
    from .game_server_status import GameServerStatus

class GameServer(Intangible):
    """
Server that provides game interaction in a multiplayer game.
    """
    class_: Literal['https://schema.org/GameServer'] = Field( # type: ignore
        default='https://schema.org/GameServer',
        alias='@type',
        serialization_alias='@type'
    )
    playersOnline: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'playersOnline',
            'https://schema.org/playersOnline'
        ),
        serialization_alias='https://schema.org/playersOnline'
    )
    serverStatus: Optional[Union["GameServerStatus", List["GameServerStatus"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serverStatus',
            'https://schema.org/serverStatus'
        ),
        serialization_alias='https://schema.org/serverStatus'
    )
    game: Optional[Union["VideoGame", List["VideoGame"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'game',
            'https://schema.org/game'
        ),
        serialization_alias='https://schema.org/game'
    )
