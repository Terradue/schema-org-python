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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .aggregate_rating import AggregateRating
    from .review import Review
    from .image_object import ImageObject

class Brand(Intangible):
    """
A brand is a name used by an organization or business person for labeling a product, product group, or similar.
    """
    class_: Literal['https://schema.org/Brand'] = Field( # type: ignore
        default='https://schema.org/Brand',
        alias='@type',
        serialization_alias='@type'
    )
    review: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'slogan',
            'https://schema.org/slogan'
        ),
        serialization_alias='https://schema.org/slogan'
    )
