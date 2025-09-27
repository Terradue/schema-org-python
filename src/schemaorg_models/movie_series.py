from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work_series import CreativeWorkSeries

from schemaorg_models.person import Person
from schemaorg_models.performing_group import PerformingGroup
from schemaorg_models.organization import Organization
from schemaorg_models.video_object import VideoObject

class MovieSeries(CreativeWorkSeries):
    """
A series of movies. Included movies can be indicated with the hasPart property.
    """
    type_: Literal['https://schema.org/MovieSeries'] = Field(default='https://schema.org/MovieSeries', alias='@type', serialization_alias='@type') # type: ignore
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'), serialization_alias='https://schema.org/musicBy')
    director: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('director', 'https://schema.org/director'), serialization_alias='https://schema.org/director')
    directors: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('directors', 'https://schema.org/directors'), serialization_alias='https://schema.org/directors')
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(default=None, validation_alias=AliasChoices('actor', 'https://schema.org/actor'), serialization_alias='https://schema.org/actor')
    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('productionCompany', 'https://schema.org/productionCompany'), serialization_alias='https://schema.org/productionCompany')
    actors: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('actors', 'https://schema.org/actors'), serialization_alias='https://schema.org/actors')
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = Field(default=None, validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'), serialization_alias='https://schema.org/trailer')
