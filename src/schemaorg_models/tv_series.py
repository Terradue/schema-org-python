from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class TVSeries(CreativeWork):
    """
CreativeWorkSeries dedicated to TV broadcast and associated online delivery.
    """
    type_: Literal['https://schema.org/TVSeries'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TVSeries'),serialization_alias='class') # type: ignore
    season: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('season', 'https://schema.org/season'),serialization_alias='https://schema.org/season')
    @field_serializer('season')
    def season2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('productionCompany', 'https://schema.org/productionCompany'),serialization_alias='https://schema.org/productionCompany')
    titleEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('titleEIDR', 'https://schema.org/titleEIDR'),serialization_alias='https://schema.org/titleEIDR')
    @field_serializer('titleEIDR')
    def titleEIDR2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'),serialization_alias='https://schema.org/musicBy')
    actors: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('actors', 'https://schema.org/actors'),serialization_alias='https://schema.org/actors')
    seasons: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = Field(default=None,validation_alias=AliasChoices('seasons', 'https://schema.org/seasons'),serialization_alias='https://schema.org/seasons')
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = Field(default=None,validation_alias=AliasChoices('countryOfOrigin', 'https://schema.org/countryOfOrigin'),serialization_alias='https://schema.org/countryOfOrigin')
    numberOfSeasons: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numberOfSeasons', 'https://schema.org/numberOfSeasons'),serialization_alias='https://schema.org/numberOfSeasons')
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = Field(default=None,validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'),serialization_alias='https://schema.org/trailer')
    directors: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('directors', 'https://schema.org/directors'),serialization_alias='https://schema.org/directors')
    episodes: Optional[Union["Episode", List["Episode"]]] = Field(default=None,validation_alias=AliasChoices('episodes', 'https://schema.org/episodes'),serialization_alias='https://schema.org/episodes')
    director: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('director', 'https://schema.org/director'),serialization_alias='https://schema.org/director')
    containsSeason: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = Field(default=None,validation_alias=AliasChoices('containsSeason', 'https://schema.org/containsSeason'),serialization_alias='https://schema.org/containsSeason')
    episode: Optional[Union["Episode", List["Episode"]]] = Field(default=None,validation_alias=AliasChoices('episode', 'https://schema.org/episode'),serialization_alias='https://schema.org/episode')
    numberOfEpisodes: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numberOfEpisodes', 'https://schema.org/numberOfEpisodes'),serialization_alias='https://schema.org/numberOfEpisodes')
    actor: Optional[Union[Person, List[Person], "PerformingGroup", List["PerformingGroup"]]] = Field(default=None,validation_alias=AliasChoices('actor', 'https://schema.org/actor'),serialization_alias='https://schema.org/actor')
