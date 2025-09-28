from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .media_gallery import MediaGallery

class ImageGallery(MediaGallery):
    """
Web page type: Image gallery page.
    """
    class_: Literal['https://schema.org/ImageGallery'] = Field( # type: ignore
        default='https://schema.org/ImageGallery',
        alias='@type',
        serialization_alias='@type'
    )
