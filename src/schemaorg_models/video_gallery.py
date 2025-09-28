from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .media_gallery import MediaGallery

class VideoGallery(MediaGallery):
    """
Web page type: Video gallery page.
    """
    class_: Literal['https://schema.org/VideoGallery'] = Field( # type: ignore
        default='https://schema.org/VideoGallery',
        alias='@type',
        serialization_alias='@type'
    )
