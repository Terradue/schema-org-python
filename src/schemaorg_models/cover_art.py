from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.visual_artwork import VisualArtwork

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CoverArt(VisualArtwork):
    """
The artwork on the outer surface of a CreativeWork.
    """
    class_: Literal['https://schema.org/CoverArt'] = Field( # type: ignore
        default='https://schema.org/CoverArt',
        alias='@type',
        serialization_alias='@type'
    )
