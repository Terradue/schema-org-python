from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class SocialEvent(Event):
    """
Event type: Social event.
    """
    class_: Literal['https://schema.org/SocialEvent'] = Field( # type: ignore
        default='https://schema.org/SocialEvent',
        alias='@type',
        serialization_alias='@type'
    )
