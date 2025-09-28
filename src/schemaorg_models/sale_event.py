from __future__ import annotations

from .event import Event    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SaleEvent(Event):
    """
Event type: Sales event.
    """
    class_: Literal['https://schema.org/SaleEvent'] = Field( # type: ignore
        default='https://schema.org/SaleEvent',
        alias='@type',
        serialization_alias='@type'
    )
