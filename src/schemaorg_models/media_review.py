from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.review import Review

from schemaorg_models.media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration
from schemaorg_models.web_page import WebPage
from schemaorg_models.media_object import MediaObject

class MediaReview(Review):
    """
A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.
    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is
    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working
    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized.
    """
    mediaAuthenticityCategory: Optional[Union[MediaManipulationRatingEnumeration, List[MediaManipulationRatingEnumeration]]] = Field(default=None,validation_alias=AliasChoices('mediaAuthenticityCategory', 'https://schema.org/mediaAuthenticityCategory'),serialization_alias='https://schema.org/mediaAuthenticityCategory')
    originalMediaLink: Optional[Union[WebPage, List[WebPage], HttpUrl, List[HttpUrl], MediaObject, List[MediaObject]]] = Field(default=None,validation_alias=AliasChoices('originalMediaLink', 'https://schema.org/originalMediaLink'),serialization_alias='https://schema.org/originalMediaLink')
    @field_serializer('originalMediaLink')
    def originalMediaLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    originalMediaContextDescription: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('originalMediaContextDescription', 'https://schema.org/originalMediaContextDescription'),serialization_alias='https://schema.org/originalMediaContextDescription')
