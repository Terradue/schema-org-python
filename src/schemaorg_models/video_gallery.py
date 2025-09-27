from typing import Literal
from pydantic import Field
from schemaorg_models.media_gallery import MediaGallery


class VideoGallery(MediaGallery):
    """
Web page type: Video gallery page.
    """
    class_: Literal['https://schema.org/VideoGallery'] = Field(default='https://schema.org/VideoGallery', alias='class', serialization_alias='class') # type: ignore
