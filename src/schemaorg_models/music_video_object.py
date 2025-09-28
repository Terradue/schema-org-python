from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.media_object import MediaObject

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MusicVideoObject(MediaObject):
    """
A music video file.
    """
    class_: Literal['https://schema.org/MusicVideoObject'] = Field( # type: ignore
        default='https://schema.org/MusicVideoObject',
        alias='@type',
        serialization_alias='@type'
    )
