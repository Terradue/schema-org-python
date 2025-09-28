from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.comic_story import ComicStory

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ComicCoverArt(ComicStory):
    """
The artwork on the cover of a comic.
    """
    class_: Literal['https://schema.org/ComicCoverArt'] = Field( # type: ignore
        default='https://schema.org/ComicCoverArt',
        alias='@type',
        serialization_alias='@type'
    )
