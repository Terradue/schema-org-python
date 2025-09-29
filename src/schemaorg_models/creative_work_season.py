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
    from .video_object import VideoObject
    from .organization import Organization
    from .creative_work_series import CreativeWorkSeries
    from .person import Person
    from .episode import Episode
    from .performing_group import PerformingGroup

class CreativeWorkSeason(CreativeWork):
    '''
    A media season, e.g. TV, radio, video game etc.

    Attributes:
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        partOfSeries: The series to which this episode or season belongs.
        episode: An episode of a TV, radio or game media within a series or season.
        numberOfEpisodes: The number of episodes in this season or series.
        endDate: The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        seasonNumber: Position of the season within an ordered group of seasons.
        episodes: An episode of a TV/radio series or season.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
        startDate: The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    '''
    class_: Literal['https://schema.org/CreativeWorkSeason'] = Field( # type: ignore
        default='https://schema.org/CreativeWorkSeason',
        alias='@type',
        serialization_alias='@type'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    partOfSeries: Optional[Union['CreativeWorkSeries', List['CreativeWorkSeries']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries',
            'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries'
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
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endDate',
            'https://schema.org/endDate'
        ),
        serialization_alias='https://schema.org/endDate'
    )
    productionCompany: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany',
            'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany'
    )
    seasonNumber: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasonNumber',
            'https://schema.org/seasonNumber'
        ),
        serialization_alias='https://schema.org/seasonNumber'
    )
    episodes: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodes',
            'https://schema.org/episodes'
        ),
        serialization_alias='https://schema.org/episodes'
    )
    trailer: Optional[Union['VideoObject', List['VideoObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trailer',
            'https://schema.org/trailer'
        ),
        serialization_alias='https://schema.org/trailer'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startDate',
            'https://schema.org/startDate'
        ),
        serialization_alias='https://schema.org/startDate'
    )
