from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

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
from schemaorg_models.thing import Thing
from schemaorg_models.web_content import WebContent
from schemaorg_models.item_list import ItemList
from schemaorg_models.list_item import ListItem
from schemaorg_models.rating import Rating

class Review(CreativeWork):
    """
A review of the item.
    """
    class_: Literal['https://schema.org/Review'] = Field( # type: ignore
        default='https://schema.org/Review',
        alias='@type',
        serialization_alias='@type'
    )
    itemReviewed: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemReviewed',
            'https://schema.org/itemReviewed'
        ),
        serialization_alias='https://schema.org/itemReviewed'
    )
    positiveNotes: Optional[Union[WebContent, List[WebContent], ItemList, List[ItemList], str, List[str], ListItem, List[ListItem]]] = Field(
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
    reviewRating: Optional[Union[Rating, List[Rating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewRating',
            'https://schema.org/reviewRating'
        ),
        serialization_alias='https://schema.org/reviewRating'
    )
    associatedReview: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedReview',
            'https://schema.org/associatedReview'
        ),
        serialization_alias='https://schema.org/associatedReview'
    )
    associatedClaimReview: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedClaimReview',
            'https://schema.org/associatedClaimReview'
        ),
        serialization_alias='https://schema.org/associatedClaimReview'
    )
    negativeNotes: Optional[Union[ListItem, List[ListItem], WebContent, List[WebContent], ItemList, List[ItemList], str, List[str]]] = Field(
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
    associatedMediaReview: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMediaReview',
            'https://schema.org/associatedMediaReview'
        ),
        serialization_alias='https://schema.org/associatedMediaReview'
    )
