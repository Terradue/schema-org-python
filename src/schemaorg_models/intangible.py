from __future__ import annotations

from .thing import Thing    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Intangible(Thing):
    """
A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.
    """
    class_: Literal['https://schema.org/Intangible'] = Field( # type: ignore
        default='https://schema.org/Intangible',
        alias='@type',
        serialization_alias='@type'
    )
