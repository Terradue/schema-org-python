from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class LiteraryEvent(Event):
    """
Event type: Literary event.
    """
    class_: Literal['https://schema.org/LiteraryEvent'] = Field( # type: ignore
        default='https://schema.org/LiteraryEvent',
        alias='@type',
        serialization_alias='@type'
    )
