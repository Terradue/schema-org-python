from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class TheaterEvent(Event):
    """
Event type: Theater performance.
    """
    class_: Literal['https://schema.org/TheaterEvent'] = Field( # type: ignore
        default='https://schema.org/TheaterEvent',
        alias='@type',
        serialization_alias='@type'
    )
