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
from .creative_work_series import CreativeWorkSeries
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .thing import Thing
    from .video_object import VideoObject
    from .postal_address import PostalAddress
    from .creative_work_season import CreativeWorkSeason
    from .organization import Organization
    from .place import Place
    from .music_group import MusicGroup
    from .creative_work import CreativeWork
    from .game_play_mode import GamePlayMode
    from .person import Person
    from .episode import Episode
    from .performing_group import PerformingGroup

class VideoGameSeries(CreativeWorkSeries):
    '''
    A video game series.

    Attributes:
        gameItem: An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.
        episode: An episode of a TV, radio or game media within a series or season.
        numberOfEpisodes: The number of episodes in this season or series.
        numberOfPlayers: Indicate how many people can play this game (minimum, maximum, or range).
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        quest: The task that a player-controlled character, or group of characters may complete in order to gain a reward.
        gameLocation: Real or fictional location of the game (or part of game).
        playMode: Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.
        season: A season in a media series.
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        musicBy: The composer of the soundtrack.
        characterAttribute: A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        seasons: A season in a media series.
        numberOfSeasons: The number of seasons in this series.
        cheatCode: Cheat codes to the game.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        containsSeason: A season that is part of the media series.
        episodes: An episode of a TV/radio series or season.
        gamePlatform: The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
    '''
    class_: Literal['https://schema.org/VideoGameSeries'] = Field( # type: ignore
        default='https://schema.org/VideoGameSeries',
        alias='@type',
        serialization_alias='@type'
    )
    gameItem: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameItem',
            'https://schema.org/gameItem'
        ),
        serialization_alias='https://schema.org/gameItem'
    )
    episode: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episode',
            'https://schema.org/episode'
        ),
        serialization_alias='https://schema.org/episode'
    )
    numberOfEpisodes: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfEpisodes',
            'https://schema.org/numberOfEpisodes'
        ),
        serialization_alias='https://schema.org/numberOfEpisodes'
    )
    numberOfPlayers: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPlayers',
            'https://schema.org/numberOfPlayers'
        ),
        serialization_alias='https://schema.org/numberOfPlayers'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    quest: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'quest',
            'https://schema.org/quest'
        ),
        serialization_alias='https://schema.org/quest'
    )
    gameLocation: Optional[Union['Place', List['Place'], HttpUrl, List[HttpUrl], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameLocation',
            'https://schema.org/gameLocation'
        ),
        serialization_alias='https://schema.org/gameLocation'
    )
    playMode: Optional[Union['GamePlayMode', List['GamePlayMode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'playMode',
            'https://schema.org/playMode'
        ),
        serialization_alias='https://schema.org/playMode'
    )
    season: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'season',
            'https://schema.org/season'
        ),
        serialization_alias='https://schema.org/season'
    )
    productionCompany: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany',
            'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany'
    )
    musicBy: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    characterAttribute: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'characterAttribute',
            'https://schema.org/characterAttribute'
        ),
        serialization_alias='https://schema.org/characterAttribute'
    )
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
    seasons: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasons',
            'https://schema.org/seasons'
        ),
        serialization_alias='https://schema.org/seasons'
    )
    numberOfSeasons: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfSeasons',
            'https://schema.org/numberOfSeasons'
        ),
        serialization_alias='https://schema.org/numberOfSeasons'
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
    containsSeason: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containsSeason',
            'https://schema.org/containsSeason'
        ),
        serialization_alias='https://schema.org/containsSeason'
    )
    episodes: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodes',
            'https://schema.org/episodes'
        ),
        serialization_alias='https://schema.org/episodes'
    )
    gamePlatform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gamePlatform',
            'https://schema.org/gamePlatform'
        ),
        serialization_alias='https://schema.org/gamePlatform'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
