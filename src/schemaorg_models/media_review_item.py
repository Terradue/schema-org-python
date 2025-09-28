from __future__ import annotations
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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .media_object import MediaObject

class MediaReviewItem(CreativeWork):
    """
Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party.
    """
    class_: Literal['https://schema.org/MediaReviewItem'] = Field( # type: ignore
        default='https://schema.org/MediaReviewItem',
        alias='@type',
        serialization_alias='@type'
    )
    mediaItemAppearance: Optional[Union["MediaObject", List["MediaObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mediaItemAppearance',
            'https://schema.org/mediaItemAppearance'
        ),
        serialization_alias='https://schema.org/mediaItemAppearance'
    )
