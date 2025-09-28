from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .person import Person
from .music_group import MusicGroup
from .thing import Thing
from .episode import Episode
from .organization import Organization
from .video_object import VideoObject
from .performing_group import PerformingGroup
from .place import Place
from .postal_address import PostalAddress
from .game_play_mode import GamePlayMode
from .quantitative_value import QuantitativeValue
from .creative_work_series import CreativeWorkSeries
from .creative_work_season import CreativeWorkSeason
from .creative_work import CreativeWork

class VideoGameSeries(CreativeWorkSeries):
    """
A video game series.
    """
    class_: Literal['https://schema.org/VideoGameSeries'] = Field( # type: ignore
        default='https://schema.org/VideoGameSeries',
        alias='@type',
        serialization_alias='@type'
    )
    gameItem: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameItem',
            'https://schema.org/gameItem'
        ),
        serialization_alias='https://schema.org/gameItem'
    )
    episode: Optional[Union[Episode, List[Episode]]] = Field(
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
    numberOfPlayers: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPlayers',
            'https://schema.org/numberOfPlayers'
        ),
        serialization_alias='https://schema.org/numberOfPlayers'
    )
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    quest: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'quest',
            'https://schema.org/quest'
        ),
        serialization_alias='https://schema.org/quest'
    )
    gameLocation: Optional[Union[Place, List[Place], HttpUrl, List[HttpUrl], PostalAddress, List[PostalAddress]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameLocation',
            'https://schema.org/gameLocation'
        ),
        serialization_alias='https://schema.org/gameLocation'
    )
    playMode: Optional[Union[GamePlayMode, List[GamePlayMode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'playMode',
            'https://schema.org/playMode'
        ),
        serialization_alias='https://schema.org/playMode'
    )
    season: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'season',
            'https://schema.org/season'
        ),
        serialization_alias='https://schema.org/season'
    )
    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany',
            'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany'
    )
    musicBy: Optional[Union[MusicGroup, List[MusicGroup], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    characterAttribute: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'characterAttribute',
            'https://schema.org/characterAttribute'
        ),
        serialization_alias='https://schema.org/characterAttribute'
    )
    actors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = Field(
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
    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cheatCode',
            'https://schema.org/cheatCode'
        ),
        serialization_alias='https://schema.org/cheatCode'
    )
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trailer',
            'https://schema.org/trailer'
        ),
        serialization_alias='https://schema.org/trailer'
    )
    directors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directors',
            'https://schema.org/directors'
        ),
        serialization_alias='https://schema.org/directors'
    )
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containsSeason',
            'https://schema.org/containsSeason'
        ),
        serialization_alias='https://schema.org/containsSeason'
    )
    episodes: Optional[Union[Episode, List[Episode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodes',
            'https://schema.org/episodes'
        ),
        serialization_alias='https://schema.org/episodes'
    )
    gamePlatform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gamePlatform',
            'https://schema.org/gamePlatform'
        ),
        serialization_alias='https://schema.org/gamePlatform'
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
