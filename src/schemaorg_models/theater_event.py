from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TheaterEvent(Event):
    """
Event type: Theater performance.
    """
    class_: Literal['https://schema.org/TheaterEvent'] = Field( # type: ignore
        default='https://schema.org/TheaterEvent',
        alias='@type',
        serialization_alias='@type'
    )
