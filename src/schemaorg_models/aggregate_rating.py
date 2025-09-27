from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.rating import Rating

from schemaorg_models.thing import Thing

class AggregateRating(Rating):
    """
The average rating based on multiple ratings or reviews.
    """
    class_: Literal['https://schema.org/AggregateRating'] = Field(default='https://schema.org/AggregateRating', alias='class', serialization_alias='class') # type: ignore
    reviewCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('reviewCount', 'https://schema.org/reviewCount'), serialization_alias='https://schema.org/reviewCount')
    ratingCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('ratingCount', 'https://schema.org/ratingCount'), serialization_alias='https://schema.org/ratingCount')
    itemReviewed: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('itemReviewed', 'https://schema.org/itemReviewed'), serialization_alias='https://schema.org/itemReviewed')
