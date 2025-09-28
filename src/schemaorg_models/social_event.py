from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SocialEvent(Event):
    """
Event type: Social event.
    """
    class_: Literal['https://schema.org/SocialEvent'] = Field( # type: ignore
        default='https://schema.org/SocialEvent',
        alias='@type',
        serialization_alias='@type'
    )
