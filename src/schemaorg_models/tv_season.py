from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work_season import CreativeWorkSeason

from schemaorg_models.country import Country
from schemaorg_models.tv_series import TVSeries

class TVSeason(CreativeWorkSeason):
    """
Season dedicated to TV broadcast and associated online delivery.
    """
    class_: Literal['https://schema.org/TVSeason'] = Field(default='https://schema.org/TVSeason', alias='class', serialization_alias='class') # type: ignore
    countryOfOrigin: Optional[Union[Country, List[Country]]] = Field(default=None, validation_alias=AliasChoices('countryOfOrigin', 'https://schema.org/countryOfOrigin'), serialization_alias='https://schema.org/countryOfOrigin')
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = Field(default=None, validation_alias=AliasChoices('partOfTVSeries', 'https://schema.org/partOfTVSeries'), serialization_alias='https://schema.org/partOfTVSeries')
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

