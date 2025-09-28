from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .audience import Audience

class Researcher(Audience):
    """
Researchers.
    """
    class_: Literal['https://schema.org/Researcher'] = Field( # type: ignore
        default='https://schema.org/Researcher',
        alias='@type',
        serialization_alias='@type'
    )
