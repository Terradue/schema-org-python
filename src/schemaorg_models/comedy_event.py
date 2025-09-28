from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class ComedyEvent(Event):
    """
Event type: Comedy event.
    """
    class_: Literal['https://schema.org/ComedyEvent'] = Field( # type: ignore
        default='https://schema.org/ComedyEvent',
        alias='@type',
        serialization_alias='@type'
    )
