from __future__ import annotations

from .clip import Clip    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RadioClip(Clip):
    """
A short radio program or a segment/part of a radio program.
    """
    class_: Literal['https://schema.org/RadioClip'] = Field( # type: ignore
        default='https://schema.org/RadioClip',
        alias='@type',
        serialization_alias='@type'
    )
