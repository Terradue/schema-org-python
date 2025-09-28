from __future__ import annotations

from .intangible import Intangible    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Language(Intangible):
    """
A sub property of instrument. The language used on this action.
    """
    class_: Literal['https://schema.org/Language'] = Field( # type: ignore
        default='https://schema.org/Language',
        alias='@type',
        serialization_alias='@type'
    )
