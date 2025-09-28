from __future__ import annotations

from .resort import Resort    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SkiResort(Resort):
    """
A ski resort.
    """
    class_: Literal['https://schema.org/SkiResort'] = Field( # type: ignore
        default='https://schema.org/SkiResort',
        alias='@type',
        serialization_alias='@type'
    )
