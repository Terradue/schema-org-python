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
    from .creative_work_season import CreativeWorkSeason
    from .hyper_toc_entry import HyperTocEntry
    from .music_group import MusicGroup
    from .creative_work_series import CreativeWorkSeries
    from .person import Person
    from .episode import Episode
    from .performing_group import PerformingGroup

class Clip(CreativeWork):
    '''
    A short TV or radio program or a segment/part of a program.

    Attributes:
        clipNumber: Position of the clip within an ordered group of clips.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        partOfEpisode: The episode to which this clip belongs.
        partOfSeries: The series to which this episode or season belongs.
        endOffset: The end time of the clip expressed as the number of seconds from the beginning of the work.
        partOfSeason: The season to which this episode belongs.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        startOffset: The start time of the clip expressed as the number of seconds from the beginning of the work.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        musicBy: The composer of the soundtrack.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
    '''
    class_: Literal['https://schema.org/Clip'] = Field( # type: ignore
        default='https://schema.org/Clip',
        alias='@type',
        serialization_alias='@type'
    )
    clipNumber: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'clipNumber',
            'https://schema.org/clipNumber'
        ),
        serialization_alias='https://schema.org/clipNumber'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    partOfEpisode: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfEpisode',
            'https://schema.org/partOfEpisode'
        ),
        serialization_alias='https://schema.org/partOfEpisode'
    )
    partOfSeries: Optional[Union['CreativeWorkSeries', List['CreativeWorkSeries']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries',
            'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries'
    )
    endOffset: Optional[Union['HyperTocEntry', List['HyperTocEntry'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endOffset',
            'https://schema.org/endOffset'
        ),
        serialization_alias='https://schema.org/endOffset'
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
    startOffset: Optional[Union[float, List[float], 'HyperTocEntry', List['HyperTocEntry']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startOffset',
            'https://schema.org/startOffset'
        ),
        serialization_alias='https://schema.org/startOffset'
    )
    actors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
    musicBy: Optional[Union['MusicGroup', List['MusicGroup'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    directors: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directors',
            'https://schema.org/directors'
        ),
        serialization_alias='https://schema.org/directors'
    )
