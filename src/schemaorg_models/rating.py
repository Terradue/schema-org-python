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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .organization import Organization

class Rating(Intangible):
    '''
    A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

    Attributes:
        bestRating: The highest value allowed in this rating system.
        reviewAspect: This Review or Rating is relevant to this part or facet of the itemReviewed.
        author: The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.
        ratingValue: The rating for the content.\
\
Usage guidelines:\
\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        worstRating: The lowest value allowed in this rating system.
        ratingExplanation: A short explanation (e.g. one to two sentences) providing background context and other information that led to the conclusion expressed in the rating. This is particularly applicable to ratings associated with "fact check" markup using [[ClaimReview]].
    '''
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
    author: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
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
