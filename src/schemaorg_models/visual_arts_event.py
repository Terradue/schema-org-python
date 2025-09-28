from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class VisualArtsEvent(Event):
    """
Event type: Visual arts event.
    """
    class_: Literal['https://schema.org/VisualArtsEvent'] = Field( # type: ignore
        default='https://schema.org/VisualArtsEvent',
        alias='@type',
        serialization_alias='@type'
    )
