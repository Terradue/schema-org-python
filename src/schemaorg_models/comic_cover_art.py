from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .comic_story import ComicStory

class ComicCoverArt(ComicStory):
    """
The artwork on the cover of a comic.
    """
    class_: Literal['https://schema.org/ComicCoverArt'] = Field( # type: ignore
        default='https://schema.org/ComicCoverArt',
        alias='@type',
        serialization_alias='@type'
    )
