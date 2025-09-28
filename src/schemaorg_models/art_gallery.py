from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .entertainment_business import EntertainmentBusiness

class ArtGallery(EntertainmentBusiness):
    """
An art gallery.
    """
    class_: Literal['https://schema.org/ArtGallery'] = Field( # type: ignore
        default='https://schema.org/ArtGallery',
        alias='@type',
        serialization_alias='@type'
    )
