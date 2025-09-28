from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Photograph(CreativeWork):
    """
A photograph.
    """
    class_: Literal['https://schema.org/Photograph'] = Field( # type: ignore
        default='https://schema.org/Photograph',
        alias='@type',
        serialization_alias='@type'
    )
