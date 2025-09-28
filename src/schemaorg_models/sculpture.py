from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Sculpture(CreativeWork):
    """
A piece of sculpture.
    """
    class_: Literal['https://schema.org/Sculpture'] = Field( # type: ignore
        default='https://schema.org/Sculpture',
        alias='@type',
        serialization_alias='@type'
    )
