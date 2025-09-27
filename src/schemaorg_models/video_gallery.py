from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.media_gallery import MediaGallery


class VideoGallery(MediaGallery):
    """
Web page type: Video gallery page.
    """
    type_: Literal['https://schema.org/VideoGallery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VideoGallery'),serialization_alias='class') # type: ignore
