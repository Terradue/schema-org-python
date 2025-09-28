from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class Hackathon(Event):
    """
A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.
    """
    class_: Literal['https://schema.org/Hackathon'] = Field( # type: ignore
        default='https://schema.org/Hackathon',
        alias='@type',
        serialization_alias='@type'
    )
