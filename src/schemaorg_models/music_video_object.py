from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .media_object import MediaObject

class MusicVideoObject(MediaObject):
    """
A music video file.
    """
    class_: Literal['https://schema.org/MusicVideoObject'] = Field( # type: ignore
        default='https://schema.org/MusicVideoObject',
        alias='@type',
        serialization_alias='@type'
    )
