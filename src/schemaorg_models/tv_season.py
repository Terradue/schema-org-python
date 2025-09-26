from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work_season import CreativeWorkSeason

from schemaorg_models.country import Country
from schemaorg_models.tv_series import TVSeries

class TVSeason(CreativeWorkSeason):
    """
Season dedicated to TV broadcast and associated online delivery.
    """
    countryOfOrigin: Optional[Union[Country, List[Country]]] = Field(default=None,validation_alias=AliasChoices('countryOfOrigin', 'https://schema.org/countryOfOrigin'),serialization_alias='https://schema.org/countryOfOrigin')
    partOfTVSeries: Optional[Union[TVSeries, List[TVSeries]]] = Field(default=None,validation_alias=AliasChoices('partOfTVSeries', 'https://schema.org/partOfTVSeries'),serialization_alias='https://schema.org/partOfTVSeries')
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('titleEIDR', 'https://schema.org/titleEIDR'),serialization_alias='https://schema.org/titleEIDR')
