from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class MusicAlbumProductionType(Enumeration):
    """
Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """
    class_: Literal['https://schema.org/MusicAlbumProductionType'] = Field( # type: ignore
        default='https://schema.org/MusicAlbumProductionType',
        alias='@type',
        serialization_alias='@type'
    )
