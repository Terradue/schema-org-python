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
    from .video_object import VideoObject
    from .creative_work_season import CreativeWorkSeason
    from .organization import Organization
    from .music_group import MusicGroup
    from .person import Person
    from .episode import Episode
    from .performing_group import PerformingGroup

class RadioSeries(CreativeWorkSeries):
    '''
    CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

    Attributes:
        episode: An episode of a TV, radio or game media within a series or season.
        numberOfEpisodes: The number of episodes in this season or series.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        season: A season in a media series.
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        musicBy: The composer of the soundtrack.
        seasons: A season in a media series.
        episodes: An episode of a TV/radio series or season.
        numberOfSeasons: The number of seasons in this series.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        containsSeason: A season that is part of the media series.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
    '''
    class_: Literal['https://schema.org/RadioSeries'] = Field( # type: ignore
        default='https://schema.org/RadioSeries',
        alias='@type',
        serialization_alias='@type'
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
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
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
    seasons: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasons',
            'https://schema.org/seasons'
        ),
        serialization_alias='https://schema.org/seasons'
    )
    episodes: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodes',
            'https://schema.org/episodes'
        ),
        serialization_alias='https://schema.org/episodes'
    )
    numberOfSeasons: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfSeasons',
            'https://schema.org/numberOfSeasons'
        ),
        serialization_alias='https://schema.org/numberOfSeasons'
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
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
