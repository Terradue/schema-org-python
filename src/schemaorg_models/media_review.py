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
from .review import Review
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .web_page import WebPage
    from .media_object import MediaObject
    from .media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration

class MediaReview(Review):
    '''
    A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.
    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is
    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working
    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized.

    Attributes:
        mediaAuthenticityCategory: Indicates a MediaManipulationRatingEnumeration classification of a media object (in the context of how it was published or shared).
        originalMediaLink: Link to the page containing an original version of the content, or directly to an online copy of the original [[MediaObject]] content, e.g. video file.
        originalMediaContextDescription: Describes, in a [[MediaReview]] when dealing with [[DecontextualizedContent]], background information that can contribute to better interpretation of the [[MediaObject]].
    '''
    class_: Literal['https://schema.org/MediaReview'] = Field( # type: ignore
        default='https://schema.org/MediaReview',
        alias='@type',
        serialization_alias='@type'
    )
    mediaAuthenticityCategory: Optional[Union['MediaManipulationRatingEnumeration', List['MediaManipulationRatingEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mediaAuthenticityCategory',
            'https://schema.org/mediaAuthenticityCategory'
        ),
        serialization_alias='https://schema.org/mediaAuthenticityCategory'
    )
    originalMediaLink: Optional[Union['WebPage', List['WebPage'], HttpUrl, List[HttpUrl], 'MediaObject', List['MediaObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'originalMediaLink',
            'https://schema.org/originalMediaLink'
        ),
        serialization_alias='https://schema.org/originalMediaLink'
    )
    originalMediaContextDescription: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'originalMediaContextDescription',
            'https://schema.org/originalMediaContextDescription'
        ),
        serialization_alias='https://schema.org/originalMediaContextDescription'
    )
