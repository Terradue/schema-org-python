from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MusicEvent(Event):
    """
Event type: Music event.
    """
    class_: Literal['https://schema.org/MusicEvent'] = Field( # type: ignore
        default='https://schema.org/MusicEvent',
        alias='@type',
        serialization_alias='@type'
    )
