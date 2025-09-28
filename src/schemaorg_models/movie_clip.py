from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.clip import Clip

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MovieClip(Clip):
    """
A short segment/part of a movie.
    """
    class_: Literal['https://schema.org/MovieClip'] = Field( # type: ignore
        default='https://schema.org/MovieClip',
        alias='@type',
        serialization_alias='@type'
    )
