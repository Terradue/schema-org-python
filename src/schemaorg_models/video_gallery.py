from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.media_gallery import MediaGallery

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
