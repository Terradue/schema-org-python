from __future__ import annotations

from .media_gallery import MediaGallery    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class VideoGallery(MediaGallery):
    """
Web page type: Video gallery page.
    """
    class_: Literal['https://schema.org/VideoGallery'] = Field( # type: ignore
        default='https://schema.org/VideoGallery',
        alias='@type',
        serialization_alias='@type'
    )
