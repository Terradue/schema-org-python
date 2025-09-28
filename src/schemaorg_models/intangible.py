from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .thing import Thing

class Intangible(Thing):
    """
A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.
    """
    class_: Literal['https://schema.org/Intangible'] = Field( # type: ignore
        default='https://schema.org/Intangible',
        alias='@type',
        serialization_alias='@type'
    )
