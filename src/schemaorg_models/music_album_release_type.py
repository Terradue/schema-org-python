from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MusicAlbumReleaseType(Enumeration):
    """
The kind of release which this album is: single, EP or album.
    """
    class_: Literal['https://schema.org/MusicAlbumReleaseType'] = Field( # type: ignore
        default='https://schema.org/MusicAlbumReleaseType',
        alias='@type',
        serialization_alias='@type'
    )
