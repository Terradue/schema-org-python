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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .video_object import VideoObject
    from .creative_work_season import CreativeWorkSeason
    from .organization import Organization
    from .music_group import MusicGroup
    from .creative_work_series import CreativeWorkSeries
    from .duration import Duration
    from .person import Person
    from .performing_group import PerformingGroup

class Episode(CreativeWork):
    '''
    A media episode (e.g. TV, radio, video game) which can be part of a series or season.

    Attributes:
        partOfSeries: The series to which this episode or season belongs.
        episodeNumber: Position of the episode within an ordered group of episodes.
        partOfSeason: The season to which this episode belongs.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        musicBy: The composer of the soundtrack.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
    '''
    class_: Literal['https://schema.org/Episode'] = Field( # type: ignore
        default='https://schema.org/Episode',
        alias='@type',
        serialization_alias='@type'
    )
    partOfSeries: Optional[Union['CreativeWorkSeries', List['CreativeWorkSeries']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries',
            'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries'
    )
    episodeNumber: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodeNumber',
            'https://schema.org/episodeNumber'
        ),
        serialization_alias='https://schema.org/episodeNumber'
    )
    partOfSeason: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeason',
            'https://schema.org/partOfSeason'
        ),
        serialization_alias='https://schema.org/partOfSeason'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
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
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
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
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
