from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class MusicEvent(Event):
    """
Event type: Music event.
    """
    class_: Literal['https://schema.org/MusicEvent'] = Field( # type: ignore
        default='https://schema.org/MusicEvent',
        alias='@type',
        serialization_alias='@type'
    )
