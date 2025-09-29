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
from .creative_work_season import CreativeWorkSeason
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .country import Country
    from .tv_series import TVSeries

class TVSeason(CreativeWorkSeason):
    '''
    Season dedicated to TV broadcast and associated online delivery.

    Attributes:
        countryOfOrigin: The country of origin of something, including products as well as creative  works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        partOfTVSeries: The TV series to which this episode or season belongs.
        titleEIDR: An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing at the most general/abstract level, a work of film or television.

For example, the motion picture known as "Ghostbusters" has a titleEIDR of  "10.5240/7EC7-228A-510A-053E-CBB8-J". This title (or work) may have several variants, which EIDR calls "edits". See [[editEIDR]].

Since schema.org types like [[Movie]], [[TVEpisode]], [[TVSeason]], and [[TVSeries]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.

    '''
    class_: Literal['https://schema.org/TVSeason'] = Field( # type: ignore
        default='https://schema.org/TVSeason',
        alias='@type',
        serialization_alias='@type'
    )
    countryOfOrigin: Optional[Union['Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
    partOfTVSeries: Optional[Union['TVSeries', List['TVSeries']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfTVSeries',
            'https://schema.org/partOfTVSeries'
        ),
        serialization_alias='https://schema.org/partOfTVSeries'
    )
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'titleEIDR',
            'https://schema.org/titleEIDR'
        ),
        serialization_alias='https://schema.org/titleEIDR'
    )
