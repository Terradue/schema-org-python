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
from schemaorg_models.media_object import MediaObject

class MediaReviewItem(CreativeWork):
    """
Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party.
    """
    class_: Literal['https://schema.org/MediaReviewItem'] = Field( # type: ignore
        default='https://schema.org/MediaReviewItem',
        alias='@type',
        serialization_alias='@type'
    )
    mediaItemAppearance: Optional[Union[MediaObject, List[MediaObject]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mediaItemAppearance',
            'https://schema.org/mediaItemAppearance'
        ),
        serialization_alias='https://schema.org/mediaItemAppearance'
    )
