from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .media_object import MediaObject

class TextObject(MediaObject):
    """
A text file. The text can be unformatted or contain markup, html, etc.
    """
    class_: Literal['https://schema.org/TextObject'] = Field( # type: ignore
        default='https://schema.org/TextObject',
        alias='@type',
        serialization_alias='@type'
    )
