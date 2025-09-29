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
    from .media_object import MediaObject

class MediaReviewItem(CreativeWork):
    '''
    Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping or reviewing party.

    Attributes:
        mediaItemAppearance: In the context of a [[MediaReview]], indicates specific media item(s) that are grouped using a [[MediaReviewItem]].
    '''
    class_: Literal['https://schema.org/MediaReviewItem'] = Field( # type: ignore
        default='https://schema.org/MediaReviewItem',
        alias='@type',
        serialization_alias='@type'
    )
    mediaItemAppearance: Optional[Union['MediaObject', List['MediaObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
