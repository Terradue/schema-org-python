from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .text import Text

class CssSelectorType(Text):
    """
Text representing a CSS selector.
    """
    class_: Literal['https://schema.org/CssSelectorType'] = Field( # type: ignore
        default='https://schema.org/CssSelectorType',
        alias='@type',
        serialization_alias='@type'
    )
