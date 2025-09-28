from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class DanceEvent(Event):
    """
Event type: A social dance.
    """
    class_: Literal['https://schema.org/DanceEvent'] = Field( # type: ignore
        default='https://schema.org/DanceEvent',
        alias='@type',
        serialization_alias='@type'
    )
