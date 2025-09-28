from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Painting(CreativeWork):
    """
A painting.
    """
    class_: Literal['https://schema.org/Painting'] = Field( # type: ignore
        default='https://schema.org/Painting',
        alias='@type',
        serialization_alias='@type'
    )
