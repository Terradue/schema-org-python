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

class AmpStory(MediaObject):
    """
A creative work with a visual storytelling format intended to be viewed online, particularly on mobile devices.
    """
    class_: Literal['https://schema.org/AmpStory'] = Field( # type: ignore
        default='https://schema.org/AmpStory',
        alias='@type',
        serialization_alias='@type'
    )
