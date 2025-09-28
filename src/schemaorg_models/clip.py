from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.person import Person

class Clip(CreativeWork):
    """
A short TV or radio program or a segment/part of a program.
    """
    class_: Literal['https://schema.org/Clip'] = Field( # type: ignore
        default='https://schema.org/Clip',
        alias='@type',
        serialization_alias='@type'
    )
    clipNumber: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'clipNumber',
            'https://schema.org/clipNumber'
        ),
        serialization_alias='https://schema.org/clipNumber'
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    partOfEpisode: Optional[Union["Episode", List["Episode"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfEpisode',
            'https://schema.org/partOfEpisode'
        ),
        serialization_alias='https://schema.org/partOfEpisode'
    )
    partOfSeries: Optional[Union["CreativeWorkSeries", List["CreativeWorkSeries"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries',
            'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries'
    )
    endOffset: Optional[Union["HyperTocEntry", List["HyperTocEntry"], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endOffset',
            'https://schema.org/endOffset'
        ),
        serialization_alias='https://schema.org/endOffset'
    )
    partOfSeason: Optional[Union["CreativeWorkSeason", List["CreativeWorkSeason"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeason',
            'https://schema.org/partOfSeason'
        ),
        serialization_alias='https://schema.org/partOfSeason'
    )
    actor: Optional[Union[Person, List[Person], "PerformingGroup", List["PerformingGroup"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    startOffset: Optional[Union[float, List[float], "HyperTocEntry", List["HyperTocEntry"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startOffset',
            'https://schema.org/startOffset'
        ),
        serialization_alias='https://schema.org/startOffset'
    )
    actors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actors',
            'https://schema.org/actors'
        ),
        serialization_alias='https://schema.org/actors'
    )
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicBy',
            'https://schema.org/musicBy'
        ),
        serialization_alias='https://schema.org/musicBy'
    )
    directors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directors',
            'https://schema.org/directors'
        ),
        serialization_alias='https://schema.org/directors'
    )
