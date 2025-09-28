from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

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
