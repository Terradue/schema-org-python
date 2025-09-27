from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.episode import Episode

from schemaorg_models.tv_series import TVSeries
from schemaorg_models.language import Language
from schemaorg_models.country import Country

class TVEpisode(Episode):
    """
A TV episode which can be part of a series or season.
    """
    type_: Literal['https://schema.org/TVEpisode'] = Field(default='https://schema.org/TVEpisode', alias='@type', serialization_alias='@type') # type: ignore
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = Field(default=None, validation_alias=AliasChoices('partOfTVSeries', 'https://schema.org/partOfTVSeries'), serialization_alias='https://schema.org/partOfTVSeries')
    subtitleLanguage: Optional[Union[Language, List[Language], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('subtitleLanguage', 'https://schema.org/subtitleLanguage'), serialization_alias='https://schema.org/subtitleLanguage')
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('titleEIDR', 'https://schema.org/titleEIDR'), serialization_alias='https://schema.org/titleEIDR')
    @field_serializer('titleEIDR')
    def titleEIDR2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    countryOfOrigin: Optional[Union[Country, List[Country]]] = Field(default=None, validation_alias=AliasChoices('countryOfOrigin', 'https://schema.org/countryOfOrigin'), serialization_alias='https://schema.org/countryOfOrigin')
