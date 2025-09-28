from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class ChildrensEvent(Event):
    """
Event type: Children's event.
    """
    class_: Literal['https://schema.org/ChildrensEvent'] = Field( # type: ignore
        default='https://schema.org/ChildrensEvent',
        alias='@type',
        serialization_alias='@type'
    )
