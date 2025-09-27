from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work_series import CreativeWorkSeries

from schemaorg_models.episode import Episode
from schemaorg_models.person import Person
from schemaorg_models.performing_group import PerformingGroup
from schemaorg_models.creative_work_season import CreativeWorkSeason
from schemaorg_models.organization import Organization
from schemaorg_models.video_object import VideoObject

class RadioSeries(CreativeWorkSeries):
    """
CreativeWorkSeries dedicated to radio broadcast and associated online delivery.
    """
    class_: Literal['https://schema.org/RadioSeries'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    episode: Optional[Union[Episode, List[Episode]]] = Field(default=None,validation_alias=AliasChoices('episode', 'https://schema.org/episode'), serialization_alias='https://schema.org/episode')
    numberOfEpisodes: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numberOfEpisodes', 'https://schema.org/numberOfEpisodes'), serialization_alias='https://schema.org/numberOfEpisodes')
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(default=None,validation_alias=AliasChoices('actor', 'https://schema.org/actor'), serialization_alias='https://schema.org/actor')
    actors: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('actors', 'https://schema.org/actors'), serialization_alias='https://schema.org/actors')
    season: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('season', 'https://schema.org/season'), serialization_alias='https://schema.org/season')
    @field_serializer('season')
    def season2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('productionCompany', 'https://schema.org/productionCompany'), serialization_alias='https://schema.org/productionCompany')
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'), serialization_alias='https://schema.org/musicBy')
    seasons: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = Field(default=None,validation_alias=AliasChoices('seasons', 'https://schema.org/seasons'), serialization_alias='https://schema.org/seasons')
    episodes: Optional[Union[Episode, List[Episode]]] = Field(default=None,validation_alias=AliasChoices('episodes', 'https://schema.org/episodes'), serialization_alias='https://schema.org/episodes')
    numberOfSeasons: Optional[Union[int, List[int]]] = Field(default=None,validation_alias=AliasChoices('numberOfSeasons', 'https://schema.org/numberOfSeasons'), serialization_alias='https://schema.org/numberOfSeasons')
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = Field(default=None,validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'), serialization_alias='https://schema.org/trailer')
    directors: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('directors', 'https://schema.org/directors'), serialization_alias='https://schema.org/directors')
    containsSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = Field(default=None,validation_alias=AliasChoices('containsSeason', 'https://schema.org/containsSeason'), serialization_alias='https://schema.org/containsSeason')
    director: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('director', 'https://schema.org/director'), serialization_alias='https://schema.org/director')
