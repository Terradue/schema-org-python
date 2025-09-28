from __future__ import annotations

from .intangible import Intangible    

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
from schemaorg_models.organization import Organization

class Rating(Intangible):
    """
A rating is an evaluation on a numeric scale, such as 1 to 5 stars.
    """
    class_: Literal['https://schema.org/Rating'] = Field( # type: ignore
        default='https://schema.org/Rating',
        alias='@type',
        serialization_alias='@type'
    )
    bestRating: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bestRating',
            'https://schema.org/bestRating'
        ),
        serialization_alias='https://schema.org/bestRating'
    )
    reviewAspect: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewAspect',
            'https://schema.org/reviewAspect'
        ),
        serialization_alias='https://schema.org/reviewAspect'
    )
    author: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'author',
            'https://schema.org/author'
        ),
        serialization_alias='https://schema.org/author'
    )
    ratingValue: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ratingValue',
            'https://schema.org/ratingValue'
        ),
        serialization_alias='https://schema.org/ratingValue'
    )
    worstRating: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'worstRating',
            'https://schema.org/worstRating'
        ),
        serialization_alias='https://schema.org/worstRating'
    )
    ratingExplanation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ratingExplanation',
            'https://schema.org/ratingExplanation'
        ),
        serialization_alias='https://schema.org/ratingExplanation'
    )
