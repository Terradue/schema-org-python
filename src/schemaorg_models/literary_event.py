from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LiteraryEvent(Event):
    """
Event type: Literary event.
    """
    class_: Literal['https://schema.org/LiteraryEvent'] = Field( # type: ignore
        default='https://schema.org/LiteraryEvent',
        alias='@type',
        serialization_alias='@type'
    )
