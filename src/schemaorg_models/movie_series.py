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
    from .person import Person
    from .performing_group import PerformingGroup
    from .organization import Organization
    from .music_group import MusicGroup
    from .video_object import VideoObject

class MovieSeries(CreativeWorkSeries):
    '''
    A series of movies. Included movies can be indicated with the hasPart property.

    Attributes:
        musicBy: The composer of the soundtrack.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
    '''
    class_: Literal['https://schema.org/MovieSeries'] = Field( # type: ignore
        default='https://schema.org/MovieSeries',
        alias='@type',
        serialization_alias='@type'
    )
    musicBy: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
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
    directors: Optional[Union['Person', List['Person']]] = Field(
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
    productionCompany: Optional[Union['Organization', List['Organization']]] = Field(
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
    trailer: Optional[Union['VideoObject', List['VideoObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
