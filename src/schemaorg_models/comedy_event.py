from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ComedyEvent(Event):
    """
Event type: Comedy event.
    """
    class_: Literal['https://schema.org/ComedyEvent'] = Field( # type: ignore
        default='https://schema.org/ComedyEvent',
        alias='@type',
        serialization_alias='@type'
    )
