from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .creative_work import CreativeWork

class Drawing(CreativeWork):
    """
A picture or diagram made with a pencil, pen, or crayon rather than paint.
    """
    class_: Literal['https://schema.org/Drawing'] = Field( # type: ignore
        default='https://schema.org/Drawing',
        alias='@type',
        serialization_alias='@type'
    )
