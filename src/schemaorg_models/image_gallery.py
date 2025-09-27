from typing import Literal
from pydantic import Field
from schemaorg_models.media_gallery import MediaGallery


class ImageGallery(MediaGallery):
    """
Web page type: Image gallery page.
    """
    class_: Literal['https://schema.org/ImageGallery'] = Field(default='https://schema.org/ImageGallery', alias='@type', serialization_alias='@type') # type: ignore
