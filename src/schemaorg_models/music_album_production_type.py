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

class MusicAlbumProductionType(Enumeration):
    """
Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """
    class_: Literal['https://schema.org/MusicAlbumProductionType'] = Field( # type: ignore
        default='https://schema.org/MusicAlbumProductionType',
        alias='@type',
        serialization_alias='@type'
    )
