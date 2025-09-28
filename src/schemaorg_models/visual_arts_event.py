from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class VisualArtsEvent(Event):
    """
Event type: Visual arts event.
    """
    class_: Literal['https://schema.org/VisualArtsEvent'] = Field( # type: ignore
        default='https://schema.org/VisualArtsEvent',
        alias='@type',
        serialization_alias='@type'
    )
