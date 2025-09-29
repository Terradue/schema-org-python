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
from .game import Game
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .game_server import GameServer
    from .video_object import VideoObject
    from .performing_group import PerformingGroup
    from .thing import Thing
    from .game_play_mode import GamePlayMode
    from .music_group import MusicGroup
    from .creative_work import CreativeWork
    from .person import Person

class VideoGame(Game):
    '''
    A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.

    Attributes:
        gameTip: Links to tips, tactics, etc.
        musicBy: The composer of the soundtrack.
        gamePlatform: The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.
        cheatCode: Cheat codes to the game.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        gameServer: The server on which  it is possible to play the game.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        playMode: Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.
        gameEdition: The edition of a video game.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
    '''
    class_: Literal['https://schema.org/VideoGame'] = Field( # type: ignore
        default='https://schema.org/VideoGame',
        alias='@type',
        serialization_alias='@type'
    )
    gameTip: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameTip',
            'https://schema.org/gameTip'
        ),
        serialization_alias='https://schema.org/gameTip'
    )
    musicBy: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    gamePlatform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gamePlatform',
            'https://schema.org/gamePlatform'
        ),
        serialization_alias='https://schema.org/gamePlatform'
    )
    cheatCode: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cheatCode',
            'https://schema.org/cheatCode'
        ),
        serialization_alias='https://schema.org/cheatCode'
    )
    trailer: Optional[Union['VideoObject', List['VideoObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trailer',
            'https://schema.org/trailer'
        ),
        serialization_alias='https://schema.org/trailer'
    )
    directors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directors',
            'https://schema.org/directors'
        ),
        serialization_alias='https://schema.org/directors'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    gameServer: Optional[Union['GameServer', List['GameServer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameServer',
            'https://schema.org/gameServer'
        ),
        serialization_alias='https://schema.org/gameServer'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    playMode: Optional[Union['GamePlayMode', List['GamePlayMode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'playMode',
            'https://schema.org/playMode'
        ),
        serialization_alias='https://schema.org/playMode'
    )
    gameEdition: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameEdition',
            'https://schema.org/gameEdition'
        ),
        serialization_alias='https://schema.org/gameEdition'
    )
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
