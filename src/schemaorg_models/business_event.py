from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BusinessEvent(Event):
    """
Event type: Business event.
    """
    class_: Literal['https://schema.org/BusinessEvent'] = Field( # type: ignore
        default='https://schema.org/BusinessEvent',
        alias='@type',
        serialization_alias='@type'
    )
