from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .creative_work import CreativeWork

class Season(CreativeWork):
    """
A season in a media series.
    """
    class_: Literal['https://schema.org/Season'] = Field( # type: ignore
        default='https://schema.org/Season',
        alias='@type',
        serialization_alias='@type'
    )
