from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .rating import Rating
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .thing import Thing

class AggregateRating(Rating):
    '''
    The average rating based on multiple ratings or reviews.

    Attributes:
        reviewCount: The count of total number of reviews.
        ratingCount: The count of total number of ratings.
        itemReviewed: The item that is being reviewed/rated.
    '''
    class_: Literal['https://schema.org/AggregateRating'] = Field( # type: ignore
        default='https://schema.org/AggregateRating',
        alias='@type',
        serialization_alias='@type'
    )
    reviewCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewCount',
            'https://schema.org/reviewCount'
        ),
        serialization_alias='https://schema.org/reviewCount'
    )
    ratingCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ratingCount',
            'https://schema.org/ratingCount'
        ),
        serialization_alias='https://schema.org/ratingCount'
    )
    itemReviewed: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemReviewed',
            'https://schema.org/itemReviewed'
        ),
        serialization_alias='https://schema.org/itemReviewed'
    )
