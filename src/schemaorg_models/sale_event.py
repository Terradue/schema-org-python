from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .event import Event

class SaleEvent(Event):
    """
Event type: Sales event.
    """
    class_: Literal['https://schema.org/SaleEvent'] = Field( # type: ignore
        default='https://schema.org/SaleEvent',
        alias='@type',
        serialization_alias='@type'
    )
