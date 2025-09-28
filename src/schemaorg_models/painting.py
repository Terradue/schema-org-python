from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .creative_work import CreativeWork

class Painting(CreativeWork):
    """
A painting.
    """
    class_: Literal['https://schema.org/Painting'] = Field( # type: ignore
        default='https://schema.org/Painting',
        alias='@type',
        serialization_alias='@type'
    )
