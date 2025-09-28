from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class Festival(Event):
    """
Event type: Festival.
    """
    class_: Literal['https://schema.org/Festival'] = Field( # type: ignore
        default='https://schema.org/Festival',
        alias='@type',
        serialization_alias='@type'
    )
