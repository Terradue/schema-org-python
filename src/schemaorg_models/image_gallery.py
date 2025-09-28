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

class ImageGallery(MediaGallery):
    """
Web page type: Image gallery page.
    """
    class_: Literal['https://schema.org/ImageGallery'] = Field( # type: ignore
        default='https://schema.org/ImageGallery',
        alias='@type',
        serialization_alias='@type'
    )
