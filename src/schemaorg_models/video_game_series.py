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
    from .thing import Thing
    from .episode import Episode
    from .creative_work import CreativeWork
    from .person import Person
    from .creative_work_season import CreativeWorkSeason
    from .place import Place
    from .performing_group import PerformingGroup
    from .quantitative_value import QuantitativeValue
    from .game_play_mode import GamePlayMode
    from .organization import Organization
    from .music_group import MusicGroup
    from .postal_address import PostalAddress
    from .video_object import VideoObject

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    episode: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    numberOfEpisodes: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    numberOfPlayers: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    quest: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    gameLocation: Optional[Union['Place', List['Place'], HttpUrl, List[HttpUrl], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    playMode: Optional[Union['GamePlayMode', List['GamePlayMode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    season: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    productionCompany: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    musicBy: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    characterAttribute: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    seasons: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    numberOfSeasons: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    cheatCode: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    trailer: Optional[Union['VideoObject', List['VideoObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    directors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    containsSeason: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    episodes: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    gamePlatform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
