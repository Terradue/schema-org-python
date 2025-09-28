from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .creative_work import CreativeWork

class Manuscript(CreativeWork):
    """
A book, document, or piece of music written by hand rather than typed or printed.
    """
    class_: Literal['https://schema.org/Manuscript'] = Field( # type: ignore
        default='https://schema.org/Manuscript',
        alias='@type',
        serialization_alias='@type'
    )
