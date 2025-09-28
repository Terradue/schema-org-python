from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DanceEvent(Event):
    """
Event type: A social dance.
    """
    class_: Literal['https://schema.org/DanceEvent'] = Field( # type: ignore
        default='https://schema.org/DanceEvent',
        alias='@type',
        serialization_alias='@type'
    )
