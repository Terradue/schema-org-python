from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .collection_page import CollectionPage

class MediaGallery(CollectionPage):
    """
Web page type: Media gallery page. A mixed-media page that can contain media such as images, videos, and other multimedia.
    """
    class_: Literal['https://schema.org/MediaGallery'] = Field( # type: ignore
        default='https://schema.org/MediaGallery',
        alias='@type',
        serialization_alias='@type'
    )
