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
    from .creative_work_season import CreativeWorkSeason
    from .organization import Organization
    from .music_group import MusicGroup
    from .person import Person
    from .episode import Episode
    from .performing_group import PerformingGroup
    from .country import Country

class TVSeries(CreativeWork):
    '''
    CreativeWorkSeries dedicated to TV broadcast and associated online delivery.

    Attributes:
        season: A season in a media series.
        productionCompany: The production company or studio responsible for the item, e.g. series, video game, episode etc.
        titleEIDR: An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing at the most general/abstract level, a work of film or television.

For example, the motion picture known as "Ghostbusters" has a titleEIDR of  "10.5240/7EC7-228A-510A-053E-CBB8-J". This title (or work) may have several variants, which EIDR calls "edits". See [[editEIDR]].

Since schema.org types like [[Movie]], [[TVEpisode]], [[TVSeason]], and [[TVSeries]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.

        musicBy: The composer of the soundtrack.
        actors: An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        seasons: A season in a media series.
        countryOfOrigin: The country of origin of something, including products as well as creative  works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        numberOfSeasons: The number of seasons in this series.
        trailer: The trailer of a movie or TV/radio series, season, episode, etc.
        directors: A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        episodes: An episode of a TV/radio series or season.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        containsSeason: A season that is part of the media series.
        episode: An episode of a TV, radio or game media within a series or season.
        numberOfEpisodes: The number of episodes in this season or series.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
    '''
    class_: Literal['https://schema.org/TVSeries'] = Field( # type: ignore
        default='https://schema.org/TVSeries',
        alias='@type',
        serialization_alias='@type'
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
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'titleEIDR',
            'https://schema.org/titleEIDR'
        ),
        serialization_alias='https://schema.org/titleEIDR'
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
    seasons: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasons',
            'https://schema.org/seasons'
        ),
        serialization_alias='https://schema.org/seasons'
    )
    countryOfOrigin: Optional[Union['Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
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
    episodes: Optional[Union['Episode', List['Episode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodes',
            'https://schema.org/episodes'
        ),
        serialization_alias='https://schema.org/episodes'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    containsSeason: Optional[Union['CreativeWorkSeason', List['CreativeWorkSeason']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containsSeason',
            'https://schema.org/containsSeason'
        ),
        serialization_alias='https://schema.org/containsSeason'
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
