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
from .creative_work_season import CreativeWorkSeason
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .country import Country
    from .tv_series import TVSeries

class TVSeason(CreativeWorkSeason):
    """
Season dedicated to TV broadcast and associated online delivery.
    """
    class_: Literal['https://schema.org/TVSeason'] = Field( # type: ignore
        default='https://schema.org/TVSeason',
        alias='@type',
        serialization_alias='@type'
    )
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
    partOfTVSeries: Optional[Union["TVSeries", List["TVSeries"]]] = Field(
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
