from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work_season import CreativeWorkSeason
from schemaorg_models.person import Person
from schemaorg_models.organization import Organization

class Episode(CreativeWork):
    """
An episode of a TV, radio or game media within a series or season.
    """
    class_: Literal['https://schema.org/Episode'] = Field(default='https://schema.org/Episode', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = Field(default=None, validation_alias=AliasChoices('partOfSeries', 'https://schema.org/partOfSeries'), serialization_alias='https://schema.org/partOfSeries')
    episodeNumber: Optional[Union[str, List[str], int, List[int]]] = Field(default=None, validation_alias=AliasChoices('episodeNumber', 'https://schema.org/episodeNumber'), serialization_alias='https://schema.org/episodeNumber')
    partOfSeason: Optional[Union[CreativeWorkSeason, List[CreativeWorkSeason]]] = Field(default=None, validation_alias=AliasChoices('partOfSeason', 'https://schema.org/partOfSeason'), serialization_alias='https://schema.org/partOfSeason')
    actor: Optional[Union[Person, List[Person], "PerformingGroup", List["PerformingGroup"]]] = Field(default=None, validation_alias=AliasChoices('actor', 'https://schema.org/actor'), serialization_alias='https://schema.org/actor')
    productionCompany: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('productionCompany', 'https://schema.org/productionCompany'), serialization_alias='https://schema.org/productionCompany')
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'), serialization_alias='https://schema.org/musicBy')
    actors: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('actors', 'https://schema.org/actors'), serialization_alias='https://schema.org/actors')
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = Field(default=None, validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'), serialization_alias='https://schema.org/trailer')
    directors: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('directors', 'https://schema.org/directors'), serialization_alias='https://schema.org/directors')
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('duration', 'https://schema.org/duration'), serialization_alias='https://schema.org/duration')
    director: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('director', 'https://schema.org/director'), serialization_alias='https://schema.org/director')
