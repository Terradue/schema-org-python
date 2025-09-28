from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .visual_artwork import VisualArtwork

class CoverArt(VisualArtwork):
    """
The artwork on the outer surface of a CreativeWork.
    """
    class_: Literal['https://schema.org/CoverArt'] = Field( # type: ignore
        default='https://schema.org/CoverArt',
        alias='@type',
        serialization_alias='@type'
    )
