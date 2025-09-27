from typing import Literal
from pydantic import Field
from schemaorg_models.media_gallery import MediaGallery


class ImageGallery(MediaGallery):
    """
Web page type: Image gallery page.
    """
    class_: Literal['https://schema.org/ImageGallery'] = Field(default='https://schema.org/ImageGallery', alias='class', serialization_alias='class') # type: ignore
