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
from .episode import Episode
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .country import Country
    from .tv_series import TVSeries
    from .language import Language

class TVEpisode(Episode):
    """
A TV episode which can be part of a series or season.
    """
    class_: Literal['https://schema.org/TVEpisode'] = Field( # type: ignore
        default='https://schema.org/TVEpisode',
        alias='@type',
        serialization_alias='@type'
    )
    partOfTVSeries: Optional[Union["TVSeries", List["TVSeries"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfTVSeries',
            'https://schema.org/partOfTVSeries'
        ),
        serialization_alias='https://schema.org/partOfTVSeries'
    )
    subtitleLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subtitleLanguage',
            'https://schema.org/subtitleLanguage'
        ),
        serialization_alias='https://schema.org/subtitleLanguage'
    )
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'titleEIDR',
            'https://schema.org/titleEIDR'
        ),
        serialization_alias='https://schema.org/titleEIDR'
    )
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
