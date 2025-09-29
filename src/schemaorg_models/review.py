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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .rating import Rating
    from .list_item import ListItem
    from .web_content import WebContent
    from .thing import Thing
    from .item_list import ItemList

class Review(CreativeWork):
    '''
    A review of an item - for example, of a restaurant, movie, or store.

    Attributes:
        itemReviewed: The item that is being reviewed/rated.
        positiveNotes: Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.

In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.

The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).
        reviewAspect: This Review or Rating is relevant to this part or facet of the itemReviewed.
        reviewRating: The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating``` applies to rating given by the review. The [[aggregateRating]] property applies to the review itself, as a creative work.
        associatedReview: An associated [[Review]].
        associatedClaimReview: An associated [[ClaimReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].
        negativeNotes: Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry 

In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions 
tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].

The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).
        reviewBody: The actual body of the review.
        associatedMediaReview: An associated [[MediaReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].
    '''
    class_: Literal['https://schema.org/Review'] = Field( # type: ignore
        default='https://schema.org/Review',
        alias='@type',
        serialization_alias='@type'
    )
    itemReviewed: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemReviewed',
            'https://schema.org/itemReviewed'
        ),
        serialization_alias='https://schema.org/itemReviewed'
    )
    positiveNotes: Optional[Union['WebContent', List['WebContent'], 'ItemList', List['ItemList'], str, List[str], 'ListItem', List['ListItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'positiveNotes',
            'https://schema.org/positiveNotes'
        ),
        serialization_alias='https://schema.org/positiveNotes'
    )
    reviewAspect: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewAspect',
            'https://schema.org/reviewAspect'
        ),
        serialization_alias='https://schema.org/reviewAspect'
    )
    reviewRating: Optional[Union['Rating', List['Rating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewRating',
            'https://schema.org/reviewRating'
        ),
        serialization_alias='https://schema.org/reviewRating'
    )
    associatedReview: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedReview',
            'https://schema.org/associatedReview'
        ),
        serialization_alias='https://schema.org/associatedReview'
    )
    associatedClaimReview: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedClaimReview',
            'https://schema.org/associatedClaimReview'
        ),
        serialization_alias='https://schema.org/associatedClaimReview'
    )
    negativeNotes: Optional[Union['ListItem', List['ListItem'], 'WebContent', List['WebContent'], 'ItemList', List['ItemList'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'negativeNotes',
            'https://schema.org/negativeNotes'
        ),
        serialization_alias='https://schema.org/negativeNotes'
    )
    reviewBody: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewBody',
            'https://schema.org/reviewBody'
        ),
        serialization_alias='https://schema.org/reviewBody'
    )
    associatedMediaReview: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMediaReview',
            'https://schema.org/associatedMediaReview'
        ),
        serialization_alias='https://schema.org/associatedMediaReview'
    )
