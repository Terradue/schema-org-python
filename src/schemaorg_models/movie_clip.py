from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .clip import Clip

class MovieClip(Clip):
    """
A short segment/part of a movie.
    """
    class_: Literal['https://schema.org/MovieClip'] = Field( # type: ignore
        default='https://schema.org/MovieClip',
        alias='@type',
        serialization_alias='@type'
    )
