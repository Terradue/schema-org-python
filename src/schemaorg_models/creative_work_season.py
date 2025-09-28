from __future__ import annotations
from datetime import (
    date,
    datetime
)
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
from .person import Person
from .episode import Episode
from .organization import Organization
from .video_object import VideoObject
from .performing_group import PerformingGroup
from .creative_work_series import CreativeWorkSeries
from .creative_work import CreativeWork

class CreativeWorkSeason(CreativeWork):
    """
A media season, e.g. TV, radio, video game etc.
    """
    class_: Literal['https://schema.org/CreativeWorkSeason'] = Field( # type: ignore
        default='https://schema.org/CreativeWorkSeason',
        alias='@type',
        serialization_alias='@type'
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    partOfSeries: Optional[Union[CreativeWorkSeries, List[CreativeWorkSeries]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries',
            'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries'
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
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endDate',
            'https://schema.org/endDate'
        ),
        serialization_alias='https://schema.org/endDate'
    )
    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(
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
    episodes: Optional[Union[Episode, List[Episode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodes',
            'https://schema.org/episodes'
        ),
        serialization_alias='https://schema.org/episodes'
    )
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = Field(
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
